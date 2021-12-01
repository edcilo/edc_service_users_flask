from typing import Callable, Type

from flask import Request
from wtforms import Field
from wtforms.validators import (
    DataRequired
)
from .form import FormRequest
from users.forms.validators.exist import Exist
from users.forms.fields import ListField
from users.models import User


class MultipleSoftDeletionForm(FormRequest):
    def rules(self, request: Type[Request]) -> dict[str, Callable]:
        return {
            'ids': ListField('ids', validators=[
                DataRequired(),
                Exist(User, column='id')
            ]),
        }
