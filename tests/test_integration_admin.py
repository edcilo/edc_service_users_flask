from flask import json
from fixture import app, client
from users.repositories import userRepo


def test_user_list(client):
    res = client.get('/admin')
    assert res.status_code == 200

def test_user_create(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    res = client.post('/admin', data=data)
    assert res.status_code == 201

def test_user_detail(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    res = client.get(f'/admin/{user.id}')
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
    res = client.put(f'/admin/{user.id}', data=new_data)
    assert res.status_code == 200

def test_user_update_password(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    data = {
        'password': 'newsecret',
        'password_confirmation': 'newsecret'
    }
    res = client.put(f'/admin/{user.id}/password', data=data)
    assert res.status_code == 204

def test_user_activate(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    res = client.post(f'/admin/{user.id}/activate')
    assert res.status_code == 204

def test_user_deactivate(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    userRepo.activate(user.id)
    res = client.post(f'/admin/{user.id}/deactivate')
    assert res.status_code == 204

def test_user_soft_delete(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    res = client.delete(f'/admin/{user.id}')
    assert res.status_code == 204

def test_user_restore(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    userRepo.soft_delete(user.id)
    res = client.post(f'/admin/{user.id}/restore')
    assert res.status_code == 204

def test_user_delete(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    userRepo.soft_delete(user.id)
    res = client.delete(f'/admin/{user.id}/hard')
    assert res.status_code == 204

