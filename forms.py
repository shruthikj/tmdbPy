"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SignupForm(FlaskForm):
    """Signup form."""
    name = StringField(
        'Name',
        [DataRequired()]
    )
    email = StringField(
        'Email',
        [
            Email(message=('Not a valid email address.')),
            DataRequired()
        ]
    )
    password = PasswordField(
        'New Password', 
        [
            DataRequired(message="Please enter a password."),
            Length (
                    min = 6,
                    message=('Your password should atleast be 6 characters.')
            )
        ]
    )
    confirm = PasswordField(
        'Confirm Password',
        [
            DataRequired(message="Please re-enter your password."),
            EqualTo(
                'password', 
                message = 'Passwords must match'
            )
        ]
    )    
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    """Login form."""
    email = StringField(
        'Email',
        [
            Email(message=('Email id does not exist')),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Enter Password', 
        [
            DataRequired(message="Please enter a password.")
        ]
    )
    submit = SubmitField('Login')