from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Användarnamn',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Lösenord', validators=[DataRequired()])
    confirm_password = PasswordField('Bekräfta Lösenord',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrera')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Lösenord', validators=[DataRequired()])
    remember = BooleanField('Kom ihåg mig')
    submit = SubmitField('Logga in')
