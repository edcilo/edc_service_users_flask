from typing import Type
from flask import jsonify

from users.decorators import form_validator
from users.forms import (
    CreateForm,
    PaginateForm,
    UpdateForm,
    UpdatePasswordForm,
    MultipleSoftDeletionForm
)
from users.forms.form import FormRequest
from users.helpers.types import response as responseType
from users.repositories import userRepo
from users.serializers import UserSerializer, serializer


class AdminController():
    @form_validator(PaginateForm, method='GET')
    def list(self, form: Type[FormRequest]) -> responseType:
        params = {
            'paginate': True,
            'search': form.data.get('q'),
            'order': form.data.get('order') or 'desc',
            'order_column': form.data.get('order_column') or 'created_at',
            'page': form.data.get('page') or 1,
            'per_page': form.data.get('per_page') or 15,
        }
        collection = userRepo.all(**params)
        serializer = UserSerializer(collection, paginate=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(PaginateForm, method='GET')
    def trash(self, form: Type[FormRequest]) -> responseType:
        params = {
            'paginate': True,
            'search': form.data.get('q'),
            'order': form.data.get('order') or 'desc',
            'order_column': form.data.get('order_column') or 'created_at',
            'page': form.data.get('page') or 1,
            'per_page': form.data.get('per_page') or 15,
            'deleted': True
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

    @form_validator(MultipleSoftDeletionForm)
    def multiple_soft_deletion(self, form: Type[FormRequest]) -> responseType:
        userRepo.multiple_soft_deletion(form.data.get('ids'))
        return jsonify(), 204

    def restore(self, id: str) -> responseType:
        userRepo.soft_delete(id, clear=True, fail=True)
        return jsonify(), 204

    @form_validator(MultipleSoftDeletionForm)
    def multiple_restore(self, form: Type[FormRequest]) -> responseType:
        userRepo.multiple_soft_deletion(form.data.get('ids'), clear=True)
        return jsonify(), 204

    def delete(self, id: str) -> responseType:
        userRepo.delete(id, fail=True)
        return jsonify({}), 204

    @form_validator(MultipleSoftDeletionForm)
    def multiple_deletion(self, form: Type[FormRequest]) -> responseType:
        userRepo.multiple_deletion(form.data.get('ids'))
        return jsonify(), 204
