from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_login import current_user
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from application.models import User

class SelectMethodForm(FlaskForm):
    methods = RadioField('methods', validators=[DataRequired()], choices=[('LibrarySearch', ''), ("ImportDeconv", ""), 
                                ('DeconvLibrarySearch', '')], default='LibrarySearch')
    submit = SubmitField('Choose')

class AcquisitionForm(FlaskForm):
    sampleLocation = StringField('Sample Location', validators=[DataRequired()])

    sampleType = StringField('Sample Type', validators=[DataRequired()])

    sampledata = StringField('Sample Data', validators=[DataRequired()])

    brand = StringField('Brand', validators=[DataRequired()])

    source = StringField('Source', validators=[DataRequired()])

    model = StringField('Model', validators=[DataRequired()])

    ionisation = StringField('Ionisation', validators=[DataRequired()])

    systemBrand = StringField('System Brand', validators=[DataRequired()])

    systemClass = StringField('System Class', validators=[DataRequired()])

    componentBrand = StringField('Component Brand', validators=[DataRequired()])

    component = StringField('Component', validators=[DataRequired()])

    componentModel = StringField('Component Model', validators=[DataRequired()])

    colBrand = StringField('Brand', validators=[DataRequired()])

    colPhase = StringField('Phase', validators=[DataRequired()])

    colPoreSizeA = StringField('Pore Size (Å)', validators=[DataRequired()])

    colPoreSizeU = StringField('Particle Size (µm)', validators=[DataRequired()])

    colLength = StringField('Length (mm)', validators=[DataRequired()])

    colDiameter = StringField('Inner Diameter (mm)', validators=[DataRequired()])

    submit = SubmitField('Save Job')
    
class LibrarySearch(AcquisitionForm):
    txtFile = FileField('User Spectra',
                            validators=[FileRequired(), FileAllowed(['txt'])])

class ImportDeconv(AcquisitionForm):
    xlsxFile = FileField('Target',
                        validators=[FileRequired(), FileAllowed(['xlsx'])])

    VANFileLow = FileField('HRMS Data (Low Energy)',
                            validators=[FileRequired(), FileAllowed(['cdf'])])

    VANFileHigh = FileField('HRMS Data (High Energy)',
                            validators=[FileRequired(), FileAllowed(['cdf'])])

class DeconvLibrarySearch(AcquisitionForm):
    xlsxFile = FileField('Target',
                        validators=[FileRequired(), FileAllowed(['xlsx'])])

    VANFileLow = FileField('HRMS Data (Low Energy)',
                            validators=[FileRequired(), FileAllowed(['cdf'])])

    VANFileHigh = FileField('HRMS Data (High Energy)',
                            validators=[FileRequired(), FileAllowed(['cdf'])])

    txtFile = FileField('User Spectra',
                            validators=[FileRequired(), FileAllowed(['txt'])])

class AlgorithmnForm(FlaskForm):
    submit = SubmitField('Process Job Now')