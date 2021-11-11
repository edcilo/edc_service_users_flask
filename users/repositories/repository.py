from flask_sqlalchemy import Model
from users.db import db


class Repository():
    _model = None

    # TODO: create abstract method
    # def __init__(self, model: Model): -> None:
    # self._model = model

    def db_save(self, model: Model) -> None:
        db.session.add(model)
        db.session.commit()

    def db_delete(self, model: Model) -> None:
        db.session.delete(model)
        db.session.commit()
