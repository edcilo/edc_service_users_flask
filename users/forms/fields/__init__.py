from wtforms import Field


class ListField(Field):
    def process_formdata(self, valuelist):
        self.data = valuelist
