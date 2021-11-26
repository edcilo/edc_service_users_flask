from flask import json
from fixture import app, client


def test_index(client):
    res = client.get('/about')
    data = json.loads(res.data)
    assert res.status_code == 200
    assert res.content_type == 'application/json'
    assert list(data.keys()) == ['code', 'data']

