from flask import Response, jsonify

from users.decorators import form_validator
from users.forms import LoginForm, RegisterForm
from users.helpers.jwt import jwtHelper
from users.repositories import userRepo
from users.serializers import JwtSerializer


class AuthController():
    @form_validator(LoginForm)
    def login(self, form) -> tuple[Response, int]:
        username = form.data.get('username')
        password = form.data.get('password')
        user = userRepo.find_optional({
            'username': username,
            'email': username,
            'phone': username
        }, fail=True)
        if not user.verify_password(password):
            return jsonify({
                'message': 'The credentials do not match our records.'
            }), 400
        serializer = JwtSerializer(user)
        token = jwtHelper.get_tokens(serializer.get_data())
        return jsonify(token), 200

    @form_validator(RegisterForm)
    def register(self, form) -> tuple[Response, int]:
        user = userRepo.add(form.data)
        serializer = JwtSerializer(user)
        token = jwtHelper.get_tokens(serializer.get_data())
        return jsonify(token, 200)

    def refresh(self) -> tuple[Response, int]:
        return jsonify({}), 200
