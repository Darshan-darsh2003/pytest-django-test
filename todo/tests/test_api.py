import requests
from utils import MockRequests

BASE_URL = 'http://localhost:8000/todo'
    
def test_create_task():
    task = MockRequests().create_random_task()
    response = requests.put(f'{BASE_URL}/create-task/', json={'title': task['title'], 'description': task['description'], 'user_id': task['user_id']})
    assert response.status_code == 201
    assert 'task_id' in response.json()

def test_get_task():
    task_id = 1  # Make sure a task with this ID exists
    response = requests.get(f'{BASE_URL}/get-task/{task_id}/')
    assert response.status_code == 200
    print(response.json())
    assert 'title' in response.json()

def test_list_tasks():
    user_id = 1  # Make sure this user ID has tasks
    response = requests.get(f'{BASE_URL}/list-tasks/{user_id}/')
    print(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task():
    response = requests.put(f'{BASE_URL}/update-task/', json={'task_id': 1, 'title': 'sadfasdfsafd sdfasdfasdfsad'})
    assert response.status_code == 200
    assert 'task_id' in response.json()

def test_delete_task():
    task_id =11  # Make sure a task with this ID exists
    response = requests.delete(f'{BASE_URL}/delete-task/{task_id}/')
    print(response)
    assert response.status_code == 204
