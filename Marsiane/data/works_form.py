from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, IntegerField, StringField, DateTimeField
from wtforms.validators import DataRequired

class WorksForm(FlaskForm):
    team_leader = IntegerField('ID руководителя', validators=[DataRequired()])
    job = StringField('Работа', validators=[DataRequired()])
    work_size = IntegerField('Размер работы', validators=[DataRequired()])
    collaborators = StringField('Участники', validators=[DataRequired()])
    is_finished = BooleanField('Закончена ли работа', validators=[DataRequired()])
    submit = SubmitField('Добавить')