from collections.abc import Iterable
from typing import Optional, Type
from wtforms.validators import ValidationError
from flask_sqlalchemy import Model


class Exist():
    def __init__(self, model: Type[Model],
                 column: Optional[str] = None,
                 message: Optional[str] = 'The selected field is invalid') -> None:
        self.model = model
        self.column = column
        self.message = message

    def __call__(self, form, field) -> None:
        column = self.column or field.name
        data = field.data if isinstance(field.data, Iterable) else [field.data]
        length = len(data)
        attribute = getattr(self.model, column)
        total = self.model.query.filter(attribute.in_(data)).count()
        if total != length:
            raise ValidationError(self.message)
