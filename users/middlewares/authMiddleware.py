from typing import Type
from flask import abort, Request
from users.helpers.jwt import jwtHelper
from users.repositories import userRepo
from .middleware import MiddlewareBase


class AuthMiddleware(MiddlewareBase):
    def handler(self, request: Type[Request]) -> None:
        auth = request.headers.get('Authorization')

        if not auth:
            abort(403)

        valid = jwtHelper.check(auth)

        if not valid:
            abort(403)

        payload = jwtHelper.decode(auth)
        payload['user'] = userRepo.find(payload['id'], fail=True)

        setattr(request, 'auth', payload)
