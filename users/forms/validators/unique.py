from typing import Type, Union
from wtforms.validators import ValidationError
from users.db import db


class Unique():
    def __init__(self, model: Type[db.Model],
                 column: Union[str, None] = None,
                 except_id: Union[int, str, None] = None,
                 message: Union[str, None] = None) -> None:
        self.model = model
        self.column = column
        self.message = message
        self.except_id = except_id

    def __call__(self, form, field) -> None:
        column = self.column or field.name
        message = self.message or f'The {field.data} has already been taken'
        filters = [getattr(self.model, column) == field.data]
        if self.except_id is not None:
            filters.append(self.model.id != self.except_id)
        exists = self.model.query.filter(*filters).count()
        if exists:
            raise ValidationError(message)
