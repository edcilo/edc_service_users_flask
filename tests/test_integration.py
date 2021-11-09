from flask import json
from fixture import app, client


def test_index(client):
    response = client.get('/')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert list(data.keys()) == ['code', 'data']

