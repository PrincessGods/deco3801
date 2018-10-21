from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_login import current_user
from wtforms import StringField, SubmitField, RadioField, FloatField, BooleanField, IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError, NumberRange

class PostForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])

    content = StringField('Content:', validators=[DataRequired()])

    submit = SubmitField('Post')