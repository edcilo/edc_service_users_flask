import uuid
from flask import jsonify, Response
from users.decorators import form_validator
from users.forms import BaseForm, CreateForm, PaginateForm, UpdateForm
from users.repositories import userRepo
from users.serializers import UserSerializer


class UserController():
    @form_validator(PaginateForm, method='GET')
    def list(self, form) -> tuple[Response, int]:
        params = {
            'paginate': True,
            'search': form.data['q'],
            'order': form.data['order'] or 'desc',
            'page': form.data['page'] or 1,
            'per_page': form.data['per_page'] or 15,
        }
        collection = userRepo.all(**params)
        serializer = UserSerializer(collection, paginate=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(CreateForm)
    def create(self, form: BaseForm) -> tuple[Response, int]:
        return jsonify({}), 200

    def detail(self, id: uuid) -> tuple[Response, int]:
        return jsonify({}), 200

    @form_validator(UpdateForm)
    def update(self, id: uuid, form: BaseForm) -> tuple[Response, int]:
        return jsonify({}), 200

    def delete(self, id: uuid) -> tuple[Response, int]:
        return jsonify({}), 200
