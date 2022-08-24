from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, SelectField, StringField, DateTimeField, IntegerField
from wtforms.validators import DataRequired


class TournamentForm(FlaskForm):
    title = StringField('Название')
    level = SelectField('Класс', choices=[5, 6, 7, 8, 9, 10, 11])
    submit = SubmitField('Добавить')