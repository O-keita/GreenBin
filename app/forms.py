from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, DateField
from wtforms.validators import DataRequired, EqualTo


class RegistrationForm(FlaskForm):
    name =StringField("Full Name", validators=[DataRequired()])
    
    email = StringField("Email", validators=[DataRequired()])

    sex = SelectField("Sex", choices=[('male', 'Male'), ('female', 'Female')])

    adress = StringField("Adress", validators=[DataRequired()])

    phone_number = StringField("Phone Number", validators=[DataRequired()])

    house_number = StringField("House Number", validators=[DataRequired()])

    password  = PasswordField("Password", validators=[DataRequired()])

    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password', message='Passwords must match')])

    submit = SubmitField("Register")
    
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])

    password = StringField("Password", validators=[DataRequired()])

    submit = SubmitField("Login")


class ScheduleForm(FlaskForm):
    date = DateField('Date', format="%Y-%m-%d", validators=[DataRequired()], render_kw={"placeholder": "YYYY-MM-DD"})
    type = SelectField("Type", choices=[('Plastic', 'Plastic'), ('Metal', 'Metal'), ('Glass', 'Glass'), ('Paper', 'Paper'), ('Other', 'Other')], validators=[DataRequired()])
    submit = SubmitField("Schedule")


class UpdateForm(FlaskForm):
    date = DateField('Date', format="%Y-%m-%d", validators=[DataRequired()], render_kw={"placeholder": "YYYY-MM-DD"})
    type = SelectField("Type", choices=[('Plastic', 'Plastic'), ('Metal', 'Metal'), ('Glass', 'Glass'), ('Paper', 'Paper'), ('Other', 'Other')], validators=[DataRequired()])
    submit = SubmitField("Schedule")