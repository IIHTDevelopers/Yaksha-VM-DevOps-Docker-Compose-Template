from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []
task_id_counter = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    task_data = request.json
    task = {
        "id": task_id_counter,
        "task": task_data.get("task"),
        "done": False
    }
    task_id_counter += 1
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>/done', methods=['PUT'])
def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')