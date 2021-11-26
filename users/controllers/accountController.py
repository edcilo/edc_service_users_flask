from flask import jsonify, request
from users.helpers.types import response as responseType
from users.serializers import AccountSerializer


class AccountController():
    def profile(self) -> responseType:
        user = request.auth.get('user')
        serializer = AccountSerializer(user)
        return jsonify(serializer.get_data()), 200
