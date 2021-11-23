from flask import Response, jsonify

from users.decorators import form_validator
from users.forms import BaseForm, RegisterForm
from users.helpers.jwt import jwtHelper
from users.repositories import userRepo
from users.serializers import UserSerializer, JwtSerializer


class AuthController():
    def login(self):
        return jsonify(), 200

    @form_validator(RegisterForm)
    def register(self, form):
        user = userRepo.add(form.data)
        serializer = JwtSerializer(user)
        token = jwtHelper.get_tokens(serializer.get_data())
        return jsonify(token, 200)
