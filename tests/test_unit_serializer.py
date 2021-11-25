from fixture import client
from users.repositories import userRepo
from users.serializers import UserSerializer


def test_user_serializer(client):
    user = userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': 1231231231,
        'password': 'secret'
    })
    serializer = UserSerializer(user)
    assert tuple(serializer.get_data().keys()) == ('id', 'username', 'email', 'phone', 'name', 'lastname', 'is_active', 'created_at', 'deleted_at')

def test_user_collection_serializer(client):
    user = userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': 1231231231,
        'password': 'secret'
    })
    UserSerializer(user)
    users = userRepo.all()
    serializer = UserSerializer(users, collection=True)
    assert len(serializer.get_data()) == 1
    assert type(serializer.get_data()) == list
