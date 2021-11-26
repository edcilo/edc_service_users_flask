from typing import Callable, Type

from flask import Request
from wtforms import StringField
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Length,
    Regexp,
)
from users.helpers.regex import password_regex
from users.repositories import userRepo
from .form import FormRequest
from .validators.passwordConfirmation import PasswordConfirmation


class ResetPasswordForm(FormRequest):
    def rules(self, request: Type[Request]) -> dict[str, Callable]:
        user_id = request.view_args.get('id')
        user = userRepo.find(user_id)
        return {
            'current_password': StringField('current_password', validators=[
                DataRequired(),
                PasswordConfirmation(user)
            ]),
            'password': StringField('password', validators=[
                DataRequired(),
                Length(min=6, max=255),
                Regexp(password_regex, message='The password is invalid'),
                EqualTo('password_confirmation')
            ]),
            'password_confirmation': StringField('password_confirmation',
                                                 validators=[
                                                     DataRequired(),
                                                 ])
        }
