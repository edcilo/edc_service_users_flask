from flask_sqlalchemy import Model as BaseModel


class Model(BaseModel):
    def setAttrs(self, data: dict) -> None:
        for key, value in data.items():
            setattr(self, key, value)

    def update(self, data: dict) -> None:
        self.setAttrs(data)

