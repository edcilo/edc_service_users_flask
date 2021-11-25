from typing import Any, Tuple
from flask_sqlalchemy import Model as BaseModel


class Model(BaseModel):
    _fillable: Tuple[str, ...] = ()

    def setAttrs(self, data: dict[str, Any]) -> None:
        for key, value in data.items():
            if key in self._fillable:
                setattr(self, key, value)

    def update(self, data: dict[str, Any]) -> None:
        self.setAttrs(data)
