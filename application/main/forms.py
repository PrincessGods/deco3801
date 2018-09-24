from flask_wtf import FlaskForm
import os
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError

class HomeSearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()]
                            , render_kw={"placeholder": os.environ.get('MySQL')})
    submit = SubmitField('Search')