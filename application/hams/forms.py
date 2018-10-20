from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_login import current_user
from wtforms import StringField, SubmitField, RadioField, FloatField, BooleanField, IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError, NumberRange
from application.models import User

class SelectMethodForm(FlaskForm):
    methods = RadioField('methods', validators=[DataRequired()], choices=[('LibrarySearch', ''), ('ImportDeconv', ''), 
                                ('DeconvLibrarySearch', '')], default='LibrarySearch')
    submit = SubmitField('Choose')
    
class AcquisitionForm(FlaskForm):
    ##input of sample information, the table to input: sample information and sample location
    ## input table:sample location
    sample_location_longitude = FloatField('Sample Location Longitude', validators=[DataRequired(), NumberRange()])

    sample_location_altitude = FloatField('Sample Location Altitude', validators=[DataRequired(), NumberRange()])

    sample_location_latitude = FloatField('Sample Location Latitude', validators=[DataRequired(), NumberRange()])

    sample_location_datum = FloatField('Location Datum', validators=[DataRequired(), NumberRange()])

    ## input table:sample information
    ##sample_raw_hrms_file_path = ??
    ##sample_targets_file_path = ??
    ##samplle_matrix = ??
    sample_private = BooleanField('Sample is Private?')

    sample_type = StringField('Sample Type', validators=[DataRequired()])

    sample_city = StringField('City of the Sample', validators=[DataRequired()])

    sample_country = StringField('Country of the Sample', validators=[DataRequired()])

    ##input for threshold setting
    ##input table: threshold_setting
   

   
    ## input of columns, the table to input: analytical_column
    column_phase = FloatField('Column Phase', validators=[DataRequired(), NumberRange()])

    column_particle_size = FloatField('Column Particle Size', validators=[DataRequired(), NumberRange()])

    column_length = FloatField('Column Length', validators=[DataRequired(), NumberRange()])

    column_pore_size = FloatField('Column Pore Size', validators=[DataRequired(), NumberRange()])

    column_inner_diameter = FloatField('Column Inner Diameter (mm)', validators=[DataRequired(), NumberRange()])

    column_brand = StringField('Column Brand', validators=[DataRequired()])

    column_model = StringField('Column Model', validators=[DataRequired()])


    ## input of HRMS instruments, table to input: acquisition_hrms, ms_system
    ## input table: ms_system
    hrms_system_class = StringField('HRMS Instruments Class', validators=[DataRequired()])

    hrms_system_model = StringField('HRMS Instruments Model', validators=[DataRequired()])

    hrms_system_brand = StringField('HRMS Instruments Brand', validators=[DataRequired()])

    ## input table: acquisition_hrms
    hrms_source = FloatField('HRMS Instruments Source', validators=[DataRequired(), NumberRange()])

    hrms_mode = StringField('HRMS Mode', validators=[DataRequired()])

    hrms_source_gas1 = FloatField('HRMS Source Gas 1', validators=[DataRequired(), NumberRange()])

    hrms_source_gas2 = FloatField('HRMS Source Gas 2', validators=[DataRequired(), NumberRange()])

    hrms_curtain_gas = FloatField('HRMS Curtain Gas', validators=[DataRequired(), NumberRange()])

    hrms_ionisation = FloatField('HRMS Ionisation', validators=[DataRequired(), NumberRange()])

    hrms_voltage = FloatField('HRMS Source Voltage', validators=[DataRequired(), NumberRange()])

    hrms_polarity = FloatField('HRMS Source Polarity', validators=[DataRequired(), NumberRange()])

    ## input of Chromatography System, table to input: chromatographic_condition, chrom_time, lc_system
    ##input table: chromatographic_condition
    chrom_sample_injection_volume = FloatField('Injection Volume (uL)', validators=[DataRequired(), NumberRange()])

    chrom_mobile_phase_a = FloatField('Chrom Mobile Phase A', validators=[DataRequired(), NumberRange()])

    chrom_mobile_phase_b = FloatField('Chrom Mobile Phase B', validators=[DataRequired(), NumberRange()])

    ##input table: chrom_time
    chrom_event_stage = StringField('Chrom Event Stage', validators=[DataRequired()])

    chrom_flow_rate = FloatField('Chrom Flow rate(ml)', validators=[DataRequired(), NumberRange()])

    chrom_gradient_a_or_b = FloatField('Chrom Gradient A/B', validators=[DataRequired(), NumberRange()])

    chrom_a_or_b = StringField('Chrom A/B', validators=[DataRequired()])

    chrom_oven_temperature = FloatField('Chrom Oven Temp °C', validators=[DataRequired(), NumberRange()])

    ##input table: lc_system
    chrom_system_brand = StringField('Chrom System Brand', validators=[DataRequired()])

    chrom_system_model = StringField('Chrom System Model', validators=[DataRequired()])

    chrom_system_class = StringField('Chrom System Class', validators=[DataRequired()])

    chrom_component_type = StringField('Chrom System Component', validators=[DataRequired()])

   


    ## Submit button
    submit = SubmitField('Save Job')

class LibrarySearch(AcquisitionForm):
    ## LibrarySearch reqested input files
    txtFile = FileField('User Spectra',
                                validators=[FileRequired(), FileAllowed(['txt'])])

class ImportDeconv(AcquisitionForm):
    xlsxFile = FileField('Target', 
                        validators=[FileRequired(), FileAllowed(['xlsx'])])

    VANFileLow = FileField('HRMS Data (Low Energy)',
                            validators=[FileRequired(), FileAllowed(['cdf'])])

    VANFileHigh = FileField('HRMS Data (High Energy)',
                            validators=[FileRequired(), FileAllowed(['cdf'])])

    Max_W = FloatField('Max_W', validators=[DataRequired(), NumberRange()], default=15.0)

    Min_Int = IntegerField('Min_Int', validators=[DataRequired(), NumberRange()], default=800.0)

    Retention_Window = FloatField('Retention_Window', validators=[DataRequired(), NumberRange()], default=0.01)

    R_Min = FloatField('R_Min', validators=[DataRequired(), NumberRange()], default=0.85)

    P_Max = FloatField('P_Max', validators=[DataRequired(), NumberRange()], default=0.05)

    Retention_Time_Tollerance = IntegerField('Retention_Time_Tollerance', validators=[DataRequired(), NumberRange()], default=3.0)

    Ms_P_W = FloatField('Ms_P_W', validators=[DataRequired(), NumberRange()], default=15.0)

    Mass_Tol = FloatField('Mass_Tol', validators=[DataRequired(), NumberRange()], default=13.0)

    Mass_Window = FloatField('Mass_Window', validators=[DataRequired(), NumberRange()], default=0.05)

    Signal_to_Noise = FloatField('Signal_to_Noise', validators=[DataRequired(), NumberRange()], default=0.01)

class DeconvLibrarySearch(AcquisitionForm):
    xlsxFile = FileField('Target',
                        validators=[FileRequired(), FileAllowed(['xlsx'])])

    VANFileLow = FileField('HRMS Data (Low Energy)',
                            validators=[FileRequired(), FileAllowed(['cdf'])])

    VANFileHigh = FileField('HRMS Data (High Energy)',
                            validators=[FileRequired(), FileAllowed(['cdf'])])

    txtFile = FileField('User Spectra',
                            validators=[FileRequired(), FileAllowed(['txt'])])

    Max_W = FloatField('Max_W', validators=[DataRequired(), NumberRange()], default=15.0)

    Min_Int = IntegerField('Min_Int', validators=[DataRequired(), NumberRange()], default=800.0)

    Retention_Window = FloatField('Retention_Window', validators=[DataRequired(), NumberRange()], default=0.01)

    R_Min = FloatField('R_Min', validators=[DataRequired(), NumberRange()], default=0.85)

    P_Max = FloatField('P_Max', validators=[DataRequired(), NumberRange()], default=0.05)

    Retention_Time_Tollerance = IntegerField('Retention_Time_Tollerance', validators=[DataRequired(), NumberRange()], default=3.0)

    Ms_P_W = FloatField('Ms_P_W', validators=[DataRequired(), NumberRange()], default=15.0)

    Mass_Tol = FloatField('Mass_Tol', validators=[DataRequired(), NumberRange()], default=13.0)

    Mass_Window = FloatField('Mass_Window', validators=[DataRequired(), NumberRange()], default=0.05)

    Signal_to_Noise = FloatField('Signal_to_Noise', validators=[DataRequired(), NumberRange()], default=0.01)

class AlgorithmnForm(FlaskForm):
    submit = SubmitField('Process Job Now')