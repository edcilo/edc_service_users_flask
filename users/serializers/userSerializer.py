from .serializer import Serializer


class UserSerializer(Serializer):
    response = {
        'id': str,
        'username': str,
        'email': str,
        'phone': str,
        'name': str,
        'lastname': str,
        'is_active': bool,
        'created_at': str,
        'deleted_at': str,
    }

