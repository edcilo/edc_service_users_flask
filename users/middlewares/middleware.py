from typing import Type
from flask import Request, request
from abc import ABC, abstractmethod
from functools import wraps


class MiddlewareBase(ABC):
    @abstractmethod
    def handler(self, request: Type[Request]) -> None:
        pass


def middleware(middlewareClass):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            middleware = middlewareClass()
            middleware.handler(request)

            return f(*args, **kwargs)
        return wrapper
    return decorator
