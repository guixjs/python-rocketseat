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
    "total_task": len(task_list)
  }
  return jsonify(response)



# em python os paths params são entre "<>", podendo converter colocando tipo:variavel (sem o tipo é sempre string)
@app.route("/tasks/<int:id>", methods=['GET'])
def get_one_task(id): # o parametro da rota é passado como parametro da funcao
  for t in tasks:
    if t.id == id:
      return jsonify(t.to_dict())
    return jsonify({
      "mensagem":"Não foi possível encontrar a task"
    }),404


@app.route("/task/<int:id>", methods=['PUT'])
def update_task(id):
  task = None
  data = request.get_json()

  for t in tasks:
    if t.id == id:
      task = t

  if task == None:
    return jsonify({
      "mensagem":"Não foi possível encontrar a task"
    }),404

  task.title = data['title']
  task.description = data['description']
  task.completed = data['completed']

  return jsonify({
    "mensagem":"Tarefa atualizada com sucesso"
  })


@app.route("/tasks/<int:id>",methods=['DELETE'])
def delete_task(id):
  task = None
  for t in tasks:
    if t.id == id:
      task = t
      break

  if task == None:    
    return jsonify({
      "mensagem":"Não foi possível encontrar a task"
    }),404

  tasks.remove(task)
  return jsonify({
    "mensagem":"Tarefa deletada com sucesso"
  })

if __name__ == "__main__":
  app.run(debug=True)