from typing import Type
from flask import jsonify

from users.decorators import form_validator
from users.forms import CreateForm, PaginateForm, UpdateForm, UpdatePasswordForm
from users.forms.form import FormRequest
from users.helpers.types import response as responseType
from users.repositories import userRepo
from users.serializers import UserSerializer


class UserController():
    @form_validator(UpdatePasswordForm)
    def update_password(
            self,
            id: str,
            form: Type[FormRequest]) -> responseType:
        userRepo.update_password(id, form.data.get('password'), fail=True)
        return jsonify(), 204
