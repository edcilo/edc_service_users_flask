import uuid
from flask import jsonify, Response


class UserController():
    def list(self) -> tuple[Response, int]:
        return jsonify({}), 200

    def create(self) -> tuple[Response, int]:
        return jsonify({}), 200

    def detail(self, id: uuid) -> tuple[Response, int]:
        return jsonify({}), 200

    def update(self, id: uuid) -> tuple[Response, int]:
        return jsonify({}), 200

    def delete(self, id: uuid) -> tuple[Response, int]:
        return jsonify({}), 200
