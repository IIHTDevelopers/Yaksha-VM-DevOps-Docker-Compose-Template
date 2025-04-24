import unittest
import docker
from docker.errors import NotFound, DockerException
from test.TestUtils import TestUtils


class TestDockerValidation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setup the test environment."""
        cls.test_obj = TestUtils()
        cls.client = docker.from_env()
        cls.container_name = "nginx"  # Assuming the container name is "nginx"

    def test_container_is_running(self):
        """Test if the container is running."""
        try:
            container = self.client.containers.get(self.container_name)
            result = container.status == "running"
            self.test_obj.yakshaAssert("TestContainerIsRunning", result, "functional")
            self.assertEqual(container.status, "running")
            if result:
                print("TestContainerIsRunning = Passed")
            else:
                print("TestContainerIsRunning = Failed")
        except NotFound:
            self.test_obj.yakshaAssert("TestContainerIsRunning", False, "functional")
            print(f"TestContainerIsRunning = Failed | ❌ {self.container_name} container not found.")
        except DockerException as e:
            self.test_obj.yakshaAssert("TestContainerIsRunning", False, "functional")
            print(f"TestContainerIsRunning = Failed | ❌ Docker exception: {e}")

    def test_container_name_is_nginx(self):
        """Test if the container name is 'nginx'."""
        try:
            container = self.client.containers.get(self.container_name)
            result = container.name == "nginx"
            self.test_obj.yakshaAssert("TestContainerNameIsNginx", result, "functional")
            self.assertEqual(container.name, "nginx")
            if result:
                print("TestContainerNameIsNginx = Passed")
            else:
                print("TestContainerNameIsNginx = Failed")
        except NotFound:
            self.test_obj.yakshaAssert("TestContainerNameIsNginx", False, "functional")
            print(f"TestContainerNameIsNginx = Failed | ❌ {self.container_name} container not found.")
        except DockerException as e:
            self.test_obj.yakshaAssert("TestContainerNameIsNginx", False, "functional")
            print(f"TestContainerNameIsNginx = Failed | ❌ Docker exception: {e}")

    def test_docker_daemon_running(self):
        """Test if Docker daemon is running and accessible."""
        try:
            version = self.client.version()
            result = "Version" in version
            self.test_obj.yakshaAssert("TestDockerDaemonRunning", result, "functional")
            self.assertIn("Version", version)
            if result:
                print("TestDockerDaemonRunning = Passed")
            else:
                print("TestDockerDaemonRunning = Failed")
        except DockerException as e:
            self.test_obj.yakshaAssert("TestDockerDaemonRunning", False, "functional")
            print(f"TestDockerDaemonRunning = Failed | ❌ Docker daemon not accessible: {e}")

    def test_nginx_container_running(self):
        """Test if the nginx container is running."""
        try:
            container = self.client.containers.get(self.container_name)
            result = container.status == "running"
            self.test_obj.yakshaAssert("TestNginxContainerRunning", result, "functional")
            self.assertEqual(container.status, "running")
            if result:
                print("TestNginxContainerRunning = Passed")
            else:
                print("TestNginxContainerRunning = Failed")
        except NotFound:
            self.test_obj.yakshaAssert("TestNginxContainerRunning", False, "functional")
            print(f"TestNginxContainerRunning = Failed | ❌ {self.container_name} container not found.")
        except DockerException as e:
            self.test_obj.yakshaAssert("TestNginxContainerRunning", False, "functional")
            print(f"TestNginxContainerRunning = Failed | ❌ Docker exception: {e}")

    def test_nginx_container_existence(self):
        """Test if the nginx container exists in Docker."""
        try:
            container = self.client.containers.get(self.container_name)
            result = container is not None
            self.test_obj.yakshaAssert("TestNginxContainerExistence", result, "functional")
            self.assertIsNotNone(container)
            if result:
                print("TestNginxContainerExistence = Passed")
            else:
                print("TestNginxContainerExistence = Failed")
        except NotFound:
            self.test_obj.yakshaAssert("TestNginxContainerExistence", False, "functional")
            print(f"TestNginxContainerExistence = Failed | ❌ {self.container_name} container not found.")
        except DockerException as e:
            self.test_obj.yakshaAssert("TestNginxContainerExistence", False, "functional")
            print(f"TestNginxContainerExistence = Failed | ❌ Docker exception: {e}")


if __name__ == "__main__":
    unittest.main()
