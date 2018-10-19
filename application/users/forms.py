from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name:', 
                            validators=[DataRequired(),
                            Length(min=2, max=20)])

    last_name = StringField('Last Name:', 
                            validators=[DataRequired(),
                            Length(min=2, max=20)])

    email = StringField('Email Address:', 
                            validators=[DataRequired(), 
                            Email()])

    password = PasswordField('Password:', 
                                validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password:',
                                        validators=[DataRequired(),
                                        EqualTo('password')])

    location =  StringField('Your Location:',
                                        validators=[DataRequired(),
                                        Length(min=2, max=50)])

    organisation =  StringField('Your Organisation:',
                                        validators=[DataRequired(),
                                        Length(min=2, max=50)])

    afflication =  StringField('Contact Number:',
                                        validators=[DataRequired(),
                                        Length(min=2, max=50)])

    receive_notification = BooleanField('I want to receive notification')

    private_account = BooleanField('It is a private account')

    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        email = User.query.filter_by(user_email=email.data).first()
        if email:
            raise ValidationError('This eamil has been registered')

class LoginForm(FlaskForm):
    email = StringField('Email Address:', validators=[DataRequired()])

    password = PasswordField('Password:', validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Log in')

class UpdateProfileForm(FlaskForm):
    first_name = StringField('First Name:', 
                            validators=[DataRequired(),
                            Length(min=2, max=20)])

    last_name = StringField('Last Name:', 
                            validators=[DataRequired(),
                            Length(min=2, max=20)])

    location = StringField('Location:', 
                            validators=[DataRequired(),
                            Length(min=2, max=50)])

    email = StringField('Email', 
                            validators=[DataRequired(), 
                            Email()])

    organisation =  StringField('Your Organisation:',
                                        validators=[DataRequired(),
                                        Length(min=2, max=50)])

    afflication =  StringField('Contact Number:',
                                        validators=[DataRequired(),
                                        Length(min=2, max=50)])

    picture = FileField('Update Profile Picture',
                            validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update Profile')

    def validate_email(self, email):
        if email.data != current_user.user_email:
            email = User.query.filter_by(user_email=email.data).first()
            if email:
                raise ValidationError('This eamil has been registered')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('This eamil has not been registered')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', 
                                validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
                                        validators=[DataRequired(),
                                        EqualTo('password')])
    
    submit = SubmitField('Reset Password')