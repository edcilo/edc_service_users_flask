from typing import Callable, Type

from flask import Request
from wtforms import IntegerField, StringField
from .form import FormRequest


class PaginateForm(FormRequest):
    def rules(self, request: Type[Request]) -> dict[str, Callable]:
        return {
            'q': StringField('q', validators=[]),
            'order': StringField('order', validators=[]),
            'order_column': StringField('order_column', validators=[]),
            'page': IntegerField('page', validators=[]),
            'per_page': IntegerField('per_page', validators=[])
        }
