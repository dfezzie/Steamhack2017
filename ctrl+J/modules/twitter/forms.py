from wtforms import Form, TextField
from wtforms.validators import DataRequired


class TwitterForm(Form):
    username = TextField('username', [DataRequired()])
