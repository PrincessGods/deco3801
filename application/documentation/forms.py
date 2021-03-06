from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_login import current_user
from wtforms import StringField, SubmitField, RadioField, FloatField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, EqualTo, ValidationError, NumberRange
from wtforms.widgets import TextArea

class PaperForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])

    paper_author = StringField('Author:', validators=[DataRequired()])

    paper_file = FileField('Upload Paper:',
                        validators=[FileRequired(), FileAllowed(['pdf'])])

    submit = SubmitField('Publish')

class PaperSearchForm(FlaskForm):
    select = SelectField('Select', choices=[('title', 'Title'), ('author', 'Author')], default='Title')

    search = StringField('Search', validators=[DataRequired()]
                            , render_kw={"placeholder": "Search this site"})
    submit = SubmitField('Search')