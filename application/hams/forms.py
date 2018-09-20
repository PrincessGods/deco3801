from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from application.models import User

class SelectMethodForm(FlaskForm):
    methods = RadioField('methods', choices=[('LibrarySearch', ''), ("ImportDeconv", ""), 
                                ('DeconvLibrarySearch', '')], default='LibrarySearch')
    submit = SubmitField('Choose')

class AcquisitionForm(FlaskForm):
    xlsxFile = FileField('Target',
                            validators=[FileAllowed(['xlsx'])])

    VANFileLow = FileField('HRMS Data (Low Energy)',
                            validators=[FileAllowed(['CDF'])])

    VANFileHigh = FileField('HRMS Data (High Energy)',
                            validators=[FileAllowed(['CDF'])])

    matFile = FileField('Mass Bank',
                            validators=[FileAllowed(['mat'])])

    adductsXlsxFile = FileField('Adducts',
                            validators=[FileAllowed(['xlsx'])])

    txtFile = FileField('User Spectra',
                            validators=[FileAllowed(['txt'])])

    sampleLocation = StringField('Sample Location', validators=[DataRequired()])

    sampleType = StringField('Sample Type', validators=[DataRequired()])

    sampledata = StringField('Sample Data', validators=[DataRequired()])

    brand = StringField('Brand', validators=[DataRequired()])

    source = StringField('Source', validators=[DataRequired()])

    model = StringField('Model', validators=[DataRequired()])

    ionisation = StringField('Ionisation', validators=[DataRequired()])

    Hams_class = StringField('Class', validators=[DataRequired()])

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