import unittest
import subprocess
import time
import requests
from TestUtils import TestUtils

class TestDockerToDoApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run(["docker-compose", "down"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["docker-compose", "up", "-d", "--build"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(5)  # Allow services to start

    @classmethod
    def tearDownClass(cls):
        subprocess.run(["docker-compose", "down"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def setUp(self):
        self.test_obj = TestUtils()

    def test_container_running(self):
        """
        Check if a container with 'yaksha' in its name is running.
        """
        try:
            result = subprocess.run(["docker", "ps"], stdout=subprocess.PIPE, text=True)
            container_running = any("yaksha" in line.lower() for line in result.stdout.splitlines())
            self.test_obj.yakshaAssert("TestContainerRunning", container_running, "functional")
            self.assertTrue(container_running)
        except Exception as e:
            self.test_obj.yakshaAssert("TestContainerRunning", False, "functional")
            self.fail(f"Exception: {e}")

    def test_get_empty_tasks(self):
        """
        Check if /tasks returns a 200 response.
        """
        try:
            response = requests.get("http://localhost:5000/tasks")
            result = response.status_code == 200
            self.test_obj.yakshaAssert("TestGetEmptyTasks", result, "functional")
            self.assertTrue(result)
        except Exception as e:
            self.test_obj.yakshaAssert("TestGetEmptyTasks", False, "functional")
            self.fail(f"Exception: {e}")

    def test_post_task(self):
        """
        Post a task and check response status.
        """
        try:
            response = requests.post("http://localhost:5000/tasks", json={"task": "Test Yaksha"})
            result = response.status_code == 201
            self.test_obj.yakshaAssert("TestPostTask", result, "functional")
            self.assertTrue(result)
        except Exception as e:
            self.test_obj.yakshaAssert("TestPostTask", False, "functional")
            self.fail(f"Exception: {e}")

    def test_get_task_after_post(self):
        """
        Post a task and verify it appears in the list.
        """
        try:
            requests.post("http://localhost:5000/tasks", json={"task": "Test Yaksha"})
            time.sleep(1)  # Wait a moment for backend to store
            response = requests.get("http://localhost:5000/tasks")
            data = response.json()
            result = any(task["task"] == "Test Yaksha" for task in data)
            self.test_obj.yakshaAssert("TestGetTaskAfterPost", result, "functional")
            self.assertTrue(result)
        except Exception as e:
            self.test_obj.yakshaAssert("TestGetTaskAfterPost", False, "functional")
            self.fail(f"Exception: {e}")

    def test_mark_task_done(self):
        """
        Post a task, mark it done, and verify the status.
        """
        try:
            post_resp = requests.post("http://localhost:5000/tasks", json={"task": "Yaksha Done Test"})
            task_id = post_resp.json().get("id")
            requests.put(f"http://localhost:5000/tasks/{task_id}/done")
            get_resp = requests.get("http://localhost:5000/tasks")
            data = get_resp.json()
            task = next((t for t in data if t["id"] == task_id), {})
            result = task.get("done", False) is True
            self.test_obj.yakshaAssert("TestMarkTaskDone", result, "functional")
            self.assertTrue(result)
        except Exception as e:
            self.test_obj.yakshaAssert("TestMarkTaskDone", False, "functional")
            self.fail(f"Exception: {e}")
