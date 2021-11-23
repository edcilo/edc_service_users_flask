from wtforms import StringField
from wtforms.validators import (
    DataRequired,
)
from users.models import User
from .form import FormRequest


class LoginForm(FormRequest):
    def rules(self, request):
        return {
            'username': StringField('username', validators=[
                DataRequired(),
            ]),
            'password': StringField('password', validators=[
                DataRequired(),
            ])
        }
