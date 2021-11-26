from typing import Callable, Type

from flask import Request
from wtforms import StringField
from wtforms.validators import (
    DataRequired,
)
from .form import FormRequest


class LoginForm(FormRequest):
    def rules(self, request: Type[Request]) -> dict[str, Callable]:
        return {
            'username': StringField('username', validators=[
                DataRequired(),
            ]),
            'password': StringField('password', validators=[
                DataRequired(),
            ])
        }
