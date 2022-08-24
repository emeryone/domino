from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, SelectField, StringField, DateTimeField, IntegerField
from wtforms.validators import DataRequired


class AddProblemForm(FlaskForm):
    number = SelectField('Номер', choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    submit = SubmitField('Добавить в турнир')