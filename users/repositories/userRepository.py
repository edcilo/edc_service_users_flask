from datetime import datetime
from typing import Any, Iterable, Optional, Union
from sqlalchemy import or_
from flask_sqlalchemy import Pagination
from users.models import User
from .repository import Repository


class UserRepository(Repository):
    def get_model(self) -> User:
        return User

    def deleted_filter(self, q, deleted: bool):
        if deleted:
            return q.filter(self._model.deleted_at != None)
        return q.filter(self._model.deleted_at == None)

    def activate(self, id: str, fail: bool = False) -> User:
        user = self.find(id, fail)
        if not user.is_active:
            user.is_active = True
            self.db_save(user)
        return user

    def add(self, data: dict[str, Any]) -> User:
        user = self._model(data)
        if 'password' in data:
            user.set_password(data['password'])
        self.db_save(user)
        return user

    def all(self, search: Optional[str] = None,
            order_column: str = 'created_at',
            order: str = 'desc',
            paginate: bool = False,
            page: int = 1,
            per_page: int = 15,
            deleted: bool = False) -> Union[list, Pagination]:
        column = getattr(self._model, order_column)
        order_by = getattr(column, order)
        q = self._model.query
        if search is not None:
            q = q.filter(or_(self._model.username.like(f'%{search}%'),
                             self._model.email.like(f'%{search}%'),
                             self._model.phone.like(f'%{search}%')))
        q = self.deleted_filter(q, deleted)
        q = q.order_by(order_by())
        users = q.paginate(page, per_page=per_page) if paginate else q.all()
        return users

    def deactivate(self, id: str, fail: bool = False) -> User:
        user = self.find(id, fail)
        if user.is_active:
            user.is_active = False
            self.db_save(user)
        return user

    def delete(self, id: str, fail: bool = False) -> User:
        user = self.find(id, fail=fail, deleted=True)
        self.db_delete(user)
        return user

    def find(self, id: str, fail: bool = False,
             deleted: bool = False) -> User:
        q = self._model.query.filter_by(id=id)
        q = self.deleted_filter(q, deleted)
        user = q.first_or_404() if fail else q.first()
        return user

    def find_by_attr(self, column: str, value: str, fail: bool = False,
                     deleted: bool = False) -> User:
        q = self._model.query.filter_by(**{column: value})
        q = self.deleted_filter(q, deleted)
        user = q.first_or_404() if fail else q.first()
        return user

    def find_optional(self, filter: dict[str, Any], fail: bool = False,
                      deleted: bool = False) -> User:
        filters = [
            getattr(self._model, key) == val for key,
            val in filter.items()
        ]
        q = self._model.query.filter(or_(*filters))
        q = self.deleted_filter(q, deleted)
        user = q.first_or_404() if fail else q.first()
        return user

    def soft_delete(
            self,
            id: str,
            clear: bool = False,
            fail: bool = False) -> User:
        user = self.find(id, fail=fail, deleted=clear)
        if (user.deleted_at is None and clear is False) \
                or (user.deleted_at is not None and clear is True):
            user.soft_delete(clear=clear)
            self.db_save(user)
        return user

    def multiple_soft_deletion(self, ids: str, clear: bool = False) -> None:
        deleted_at = None if clear else datetime.now()
        self._model.query.filter(self._model.id.in_(ids)).update({
            'deleted_at': deleted_at
        })
        self.db_save()

    def update(self,
               id: str,
               data: dict[str, Any],
               fail: bool = False) -> User:
        user = self.find(id, fail=fail)
        user.update(data)
        self.db_save(user)
        return user

    def update_password(
            self,
            id: str,
            password: str,
            fail: bool = False) -> User:
        user = self.find(id, fail)
        user.set_password(password)
        self.db_save(user)
        return user
