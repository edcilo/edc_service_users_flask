import abc
from typing import Type
from flask_sqlalchemy import Model
from users.db import db


class Repository(abc.ABC):
    def __init__(self) -> None:
        self._model = self.get_model()

    @abc.abstractmethod
    def get_model(self) -> Model:
        pass

    def db_save(self, model: Type[Model]) -> None:
        if callable(getattr(model, 'touch', None)):
            model.touch()
        db.session.add(model)
        db.session.commit()

    def db_delete(self, model: Type[Model]) -> None:
        db.session.delete(model)
        db.session.commit()
