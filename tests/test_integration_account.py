from flask import json
from fixture import app, client
from users.repositories import userRepo


def test_profile(client):
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
    res = client.get('/profile', headers=headers)
    assert res.status_code == 200
