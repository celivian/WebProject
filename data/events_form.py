from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired
class EventsForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    discription = StringField('Описание', validators=[DataRequired()])
    submit = SubmitField('Добавить')