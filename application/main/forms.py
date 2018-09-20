from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError

class HomeSearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()]
                            , render_kw={"placeholder": "Search this site"})
    submit = SubmitField('Search')