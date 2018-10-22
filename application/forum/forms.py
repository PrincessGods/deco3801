from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_login import current_user
from wtforms import StringField, SubmitField, RadioField, FloatField, BooleanField, IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError, NumberRange
from wtforms.widgets import TextArea

class PostForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])

    content = StringField('Content:', validators=[DataRequired()], widget=TextArea())

    submit = SubmitField('Post')

class PostSearchForm(FlaskForm):
    select = SelectField('Select', choices=[('title', 'Title'), ('contents', 'Content')], default='Title')

    search = StringField('Search', validators=[DataRequired()]
                            , render_kw={"placeholder": "Search this site"})
    submit = SubmitField('Search')