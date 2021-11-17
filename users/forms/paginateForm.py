from wtforms import IntegerField, StringField
from .form import FormRequest


class PaginateForm(FormRequest):
    def rules(self, request):
        return  {
            'q': StringField('q', validators=[]),
            'order': StringField('order',  validators=[]),
            'page': IntegerField('page', validators=[]),
            'per_page': IntegerField('per_page', validators=[])
        }

