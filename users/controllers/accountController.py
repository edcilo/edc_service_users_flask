from typing import Type
from flask import jsonify, request
from users.decorators import form_validator
from users.forms import UpdatePasswordForm
from users.forms.form import FormRequest
from users.helpers.types import response as responseType
from users.repositories import userRepo
from users.serializers import AccountSerializer


class AccountController():
    def profile(self) -> responseType:
        user = request.auth.get('user')
        serializer = AccountSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(UpdatePasswordForm)
    def update_password(
            self,
            id: str,
            form: Type[FormRequest]) -> responseType:
        userRepo.update_password(id, form.data.get('password'), fail=True)
        return jsonify(), 204
