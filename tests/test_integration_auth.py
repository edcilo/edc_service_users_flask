from flask import json
from fixture import app, client
from users.repositories import userRepo


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

def test_refresh_token(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    userRepo.add(data)
    loginres = client.post('/login', data=data)
    data = json.loads(loginres.data)
    token = data.get('token')
    headers = {'Authorization': f'Bearer {token}'}
    res = client.post('/refresh', headers=headers)
    assert res.status_code == 200

def test_refresh_check(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    userRepo.add(data)
    loginres = client.post('/login', data=data)
    data = json.loads(loginres.data)
    token = data.get('token')
    headers = {'Authorization': f'Bearer {token}'}
    res = client.post('/check', headers=headers)
    assert res.status_code == 204
