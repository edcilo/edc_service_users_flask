from typing import Type
from flask import jsonify

from users.decorators import form_validator
from users.forms import CreateForm, PaginateForm, UpdateForm, UpdatePasswordForm
from users.forms.form import FormRequest
from users.helpers.types import response as responseType
from users.repositories import userRepo
from users.serializers import UserSerializer


class AdminController():
    @form_validator(PaginateForm, method='GET')
    def list(self, form: Type[FormRequest]) -> responseType:
        params = {
            'paginate': True,
            'search': form.data['q'],
            'order': form.data['order'] or 'desc',
            'order_column': form.data['order_column'] or 'id',
            'page': form.data['page'] or 1,
            'per_page': form.data['per_page'] or 15,
        }
        collection = userRepo.all(**params)
        serializer = UserSerializer(collection, paginate=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(CreateForm)
    def create(self, form: Type[FormRequest]) -> responseType:
        user = userRepo.add(form.data)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 201

    def detail(self, id: str) -> responseType:
        user = userRepo.find(id, fail=True)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(UpdateForm)
    def update(self, id: str, form: Type[FormRequest]) -> responseType:
        user = userRepo.update(id, form.data, fail=True)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(UpdatePasswordForm)
    def update_password(self, id, form: Type[FormRequest]) -> responseType:
        userRepo.update_password(id, form.data.get('password'), fail=True)
        return jsonify(), 204

    def activate(self, id: str) -> responseType:
        userRepo.activate(id, fail=True)
        return jsonify(), 204

    def deactivate(self, id: str) -> responseType:
        userRepo.deactivate(id, fail=True)
        return jsonify(), 204

    def soft_delete(self, id: str) -> responseType:
        userRepo.soft_delete(id, fail=True)
        return jsonify(), 204

    def restore(self, id: str) -> responseType:
        userRepo.soft_delete(id, clear=True, fail=True)
        return jsonify(), 204

    def delete(self, id: str) -> responseType:
        userRepo.delete(id, fail=True)
        return jsonify({}), 204
