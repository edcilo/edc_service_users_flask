from flask import json
from fixture import app, client
from users.helpers.jwt import jwtHelper
from users.repositories import userRepo
from users.serializers import JwtSerializer


def adminuser():
    data = {
        'username': 'admin',
        'email': 'admin@example.com',
        'phone': '1231231230',
        'password': 'secret'
    }
    return userRepo.add(data)

def authtoken(user):
    serializer = JwtSerializer(user)
    return jwtHelper.get_tokens(serializer.get_data())


def test_user_list(client):
    admin = adminuser()
    token = authtoken(admin)
    headers = {'Authorization': f"Bearer {token['token']}"}
    res = client.get('/admin', headers=headers)
    assert res.status_code == 200

def test_user_create(client):
    admin = adminuser()
    token = authtoken(admin)
    headers = {'Authorization': f"Bearer {token['token']}"}
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    res = client.post('/admin', data=data, headers=headers)
    assert res.status_code == 201

def test_user_detail(client):
    admin = adminuser()
    token = authtoken(admin)
    headers = {'Authorization': f"Bearer {token['token']}"}
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    res = client.get(f'/admin/{user.id}', headers=headers)
    assert res.status_code == 200

def test_user_update(client):
    admin = adminuser()
    token = authtoken(admin)
    headers = {'Authorization': f"Bearer {token['token']}"}
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
    res = client.put(f'/admin/{user.id}', data=new_data, headers=headers)
    assert res.status_code == 200

def test_user_update_password(client):
    admin = adminuser()
    token = authtoken(admin)
    headers = {'Authorization': f"Bearer {token['token']}"}
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
    res = client.put(f'/admin/{user.id}/password', data=data, headers=headers)
    assert res.status_code == 204

def test_user_activate(client):
    admin = adminuser()
    token = authtoken(admin)
    headers = {'Authorization': f"Bearer {token['token']}"}
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    res = client.post(f'/admin/{user.id}/activate', headers=headers)
    assert res.status_code == 204

def test_user_deactivate(client):
    admin = adminuser()
    token = authtoken(admin)
    headers = {'Authorization': f"Bearer {token['token']}"}
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    userRepo.activate(user.id)
    res = client.post(f'/admin/{user.id}/deactivate', headers=headers)
    assert res.status_code == 204

def test_user_soft_delete(client):
    admin = adminuser()
    token = authtoken(admin)
    headers = {'Authorization': f"Bearer {token['token']}"}
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    res = client.delete(f'/admin/{user.id}', headers=headers)
    assert res.status_code == 204

def test_user_restore(client):
    admin = adminuser()
    token = authtoken(admin)
    headers = {'Authorization': f"Bearer {token['token']}"}
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    userRepo.soft_delete(user.id)
    res = client.post(f'/admin/{user.id}/restore', headers=headers)
    assert res.status_code == 204

def test_user_delete(client):
    admin = adminuser()
    token = authtoken(admin)
    headers = {'Authorization': f"Bearer {token['token']}"}
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    userRepo.soft_delete(user.id)
    res = client.delete(f'/admin/{user.id}/hard', headers=headers)
    assert res.status_code == 204

