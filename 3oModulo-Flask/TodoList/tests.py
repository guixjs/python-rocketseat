import requests
import pytest

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
  new_task = {
    "title": "Titulo",
    "description":"Descricao da tarefa"
  }
  response = requests.post(f"{BASE_URL}/task", json=new_task)
  assert response.status_code == 200
  res = response.json()
  assert "mensagem" in res
  assert "id" in res
  tasks.append(res['id'])

def test_get_tasks():
  response  = requests.get(f"{BASE_URL}/tasks")
  assert response.status_code == 200
  res_json = response.json()

  assert "tasks" in res_json
  assert "total_task" in res_json

def test_get_one_task():
  if tasks:
    task_id = tasks[0]
    response  = requests.get(f"{BASE_URL}/task/{task_id}")
    assert response.status_code == 200
    res_json = response.json()

    assert task_id == res_json['id']
    
def test_update_task():
  if tasks:
    task_id = tasks[0]
    payload = {
      "completed": True,
      "description": "Nova descrição",
      "title": "Título atualizado"
    }
    response  = requests.put(f"{BASE_URL}/task/{task_id}",json=payload)
    assert response.status_code == 200
    res_json = response.json()

    assert "mensagem" in res_json
    response  = requests.get(f"{BASE_URL}/task/{task_id}")
    assert response.status_code == 200
    res_json = response.json()

    assert res_json['title'] == payload['title']
    assert res_json['description'] == payload['description']
    assert res_json['completed'] == payload['completed']


def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/task/{task_id}")
        assert response.status_code == 200
        response = requests.get(f"{BASE_URL}/task/{task_id}")
        assert response.status_code == 404