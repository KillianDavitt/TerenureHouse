from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class PinForm(Form):
    user = StringField(validators=[DataRequired()])
    pin = IntegerField()
