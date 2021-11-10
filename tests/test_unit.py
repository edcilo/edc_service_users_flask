from fixture import app, client
from users.models import User


def test_user_model_fullname(client):
    data = {
        'name': 'Jhon',
        'lastname': 'Doe',}
    user = User(data)
    assert user.fullname == 'Jhon Doe'

def test_user_model_setattrs(client):
    data = {
        'username': 'jhon.doe',
        'password': 'secret'}
    user = User(data)
    assert user.username == 'jhon.doe'
    assert user.password == None

def test_user_model_update(client):
    user = User({'username': 'jhon.doe.00'})
    user.update({'username': 'jhon.doe.01'})
    assert user.username == 'jhon.doe.01'

def test_user_model_setpassword(client):
    user = User({'username': 'jhon.doe'})
    user.set_password('secret')
    assert user.password is not None
    assert user.password != 'secret'
    assert user.verify_password('secret') == True
    assert user.verify_password('test') == False

def test_user_model_repr(client):
    user = User({'email': 'jhon.doe@example.com'})
    assert str(user) == '<User None jhon.doe@example.com>'
