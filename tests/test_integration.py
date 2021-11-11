from flask import json
from fixture import app, client


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
    res = client.post('/')
    assert res.status_code == 200

def test_user_detail(client):
    res = client.get('/1')
    assert res.status_code == 200

def test_user_update(client):
    res = client.put('/1')
    assert res.status_code == 200

def test_user_delete(client):
    res = client.delete('/1')
    assert res.status_code == 200
