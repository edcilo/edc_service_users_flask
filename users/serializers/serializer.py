from typing import Iterable, Type, Any, Union
from flask_sqlalchemy import Model


class Serializer:
    response: dict[str, Type] = dict()

    def __init__(self, model: Type[Model], collection: bool = False,
                 paginate: bool = False) -> None:
        self.__original = model
        self.__model = model.items if paginate else model
        self.__is_paginated = paginate
        self.__is_collection = collection or paginate

    def get_data(self):
        data = self.handler()
        return data

    def handler(self) -> Union[dict[str, Any], list[dict[str, Any]]]:
        data = self.handler_collection(self.__model) \
            if self.__is_collection else self.serialize(self.__model)
        if self.__is_paginated:
            pagination_data = {
                'page': self.__original.page,
                'pages': self.__original.pages,
                'per_page': self.__original.per_page,
                'prev': self.__original.prev_num,
                'next': self.__original.next_num,
                'total': self.__original.total,
            }
            data = {'data': data, 'pagination': pagination_data}
        return data

    def handler_collection(
            self, collection: list[Model]) -> list[dict[str, Any]]:
        serialized = list()
        for model in collection:
            data = self.serialize(model)
            serialized.append(data)
        return serialized

    def serialize(self, model: Type[Model]) -> dict[str, Any]:
        data = {}
        for attr, type in self.response.items():
            value = getattr(model, attr, None)
            data[attr] = value if value is None else type(value)
        return data
