from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)


tasks = []
task_id_control = 1
@app.route('/task',methods=['POST'])
def create_task():
  global task_id_control
  data = request.get_json()
  new_task = Task(id=task_id_control,title=data['title'], description=data.get("description",""))
  task_id_control += 1
  tasks.append(new_task)
  return jsonify({
    "mensagem":"Nova tarefa criada com sucesso"
  })
  

@app.route("/tasks",methods=['GET'])
def get_tasks():
  task_list = []
  for t in tasks:
    task_list.append(t.to_dict())
  response = {
    "tasks":task_list,
    "total_task": 0
  }
  return jsonify(response)
if __name__ == "__main__":
  app.run(debug=True)