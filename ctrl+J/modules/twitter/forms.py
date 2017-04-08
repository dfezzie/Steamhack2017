from wtforms import Form, TextField, SubmitField
from wtforms.validators import DataRequired


class TwitterForm(Form):
    username = TextField('Username', [DataRequired()])
    submit = SubmitField('Submit')
