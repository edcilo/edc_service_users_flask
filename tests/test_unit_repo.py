from fixture import client
from users.models import User
from users.repositories import userRepo


def test_user_repo_add(client):
    user = userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret', })
    assert isinstance(user, User)
    assert user.id is not None
    assert user.password is not None

def test_user_repo_activate_and_deactivate(client):
    user = userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example',
        'phone': '1231231231',
        'password': 'secret',
    })
    assert user.is_active == False
    user = userRepo.activate(user.id, fail=True)
    assert user.is_active == True
    user = userRepo.deactivate(user.id, fail=True)
    assert user.is_active == False

def test_user_repo_find(client):
    user = userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret', })
    user_found = userRepo.find(user.id)
    assert isinstance(user_found, User)
    user_not_found = userRepo.find('foo')
    assert user_not_found is None

def test_user_repo_find_by_attr(client):
    userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret', })
    user_found = userRepo.find_by_attr('username', 'jhon.doe')
    assert isinstance(user_found, User)
    userRepo.delete(user_found.id)
    user_found = userRepo.find_by_attr('username', 'jhon.doe', with_deleted=True)
    assert user_found is not None

def test_user_repor_find_optional(client):
    userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret', })
    user_found = userRepo.find_optional({
        'username': 'jhon',
        'email': 'jhon.doe@example.com'})
    assert isinstance(user_found, User)
    assert user_found.email == 'jhon.doe@example.com'

def test_user_repo_getall(client):
    userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret', })
    users = userRepo.all()
    assert isinstance(users, list)
    assert len(users) == 1

def test_user_repo_update(client):
    user = userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret', })
    user_updated = userRepo.update(user.id, {'phone': '3213213213'})
    assert user_updated.phone == '3213213213'

def test_user_repo_delete(client):
    user = userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret', })
    userRepo.delete(user.id)
    user = userRepo.find(user.id)
    assert user is None

