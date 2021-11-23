from flask import json
from fixture import app, client
from users.repositories import userRepo


def test_index(client):
    res = client.get('/about')
    data = json.loads(res.data)
    assert res.status_code == 200
    assert res.content_type == 'application/json'
    assert list(data.keys()) == ['code', 'data']

def test_user_list(client):
    res = client.get('/')
    assert res.status_code == 200

def test_user_create(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    res = client.post('/', data=data)
    assert res.status_code == 201

def test_user_detail(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    res = client.get(f'/{user.id}')
    assert res.status_code == 200

def test_user_update(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    new_data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe.00@example.com',
        'phone': '1231231231',
    }
    res = client.put(f'/{user.id}', data=new_data)
    assert res.status_code == 200

def test_user_delete(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    res = client.delete(f'/{user.id}')
    assert res.status_code == 204

def test_register(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
        'password_confirmation': 'secret'
    }
    res = client.post('/register', data=data)
    assert res.status_code == 200

def test_login(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    userRepo.add(data)
    data = {
        'username': 'jhon.doe',
        'password': 'secret',
    }
    res = client.post('/login', data=data)
    assert res.status_code == 200

def test_bad_credentials(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    userRepo.add(data)
    data = {
        'username': 'jhon.doe',
        'password': 'secre'
    }
    res = client.post('/login', data=data)
    assert res.status_code == 400
