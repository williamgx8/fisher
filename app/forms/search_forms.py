from wtforms import StringField, IntegerField, Form
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForms(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=13, message='q参数长度不正确')])
    page = IntegerField(validators=[NumberRange(min=1, max=99, message='page参数格式错误')], default=1)
