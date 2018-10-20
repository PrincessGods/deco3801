from application import db, login_manager
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column('User_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_firstname = db.Column('User_FirstName', db.String(255), nullable=False)
    user_lastname = db.Column('User_LastName', db.String(255), nullable=False)
    user_email = db.Column('User_Email', db.String(255), nullable=False)
    user_password = db.Column('User_Password', db.String(255), nullable=False)
    user_location = db.Column('User_Location', db.String(255), nullable=False)
    user_organisation = db.Column('User_Organisation', db.String(100), nullable=False)
    user_icon = db.Column('User_Icon', db.String(40), nullable=False, default='default.jpg')
    user_affilication = db.Column('User_Affilication', db.String(255), nullable=False)
    user_receive_notification = db.Column('user_Receive_Notification', db.String(2), nullable=False)
    user_private = db.Column('User_Private', db.String(2), nullable=False)
    user_is_admin = db.Column('User_Is_Admin', db.String(2), nullable=False, default='N')
    user_approved = db.Column('User_Approved', db.String(2), nullable=False, default='Y')
    ##posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.user_firstname}', '{self.user_lastname}','{self.user_email}', '{self.user_icon}')"

class Job(db.Model, UserMixin):
    j_id = db.Column(db.String(10), primary_key=True)
    u_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Acquisition_Hrms(db.Model, UserMixin):
    __tablename__ = 'acquisition_hrms'
    id = db.Column('Acqui_Hrms_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    hrms_mode = db.Column('Hrms_Mode', db.String(255), nullable=False)
    hrms_source_gas1 = db.Column('Hrms_Source_Gas1', db.Float(10), nullable=False)
    hrms_source_gas2 = db.Column('Hrms_Source_Gas2', db.Float(10), nullable=False)
    hrms_curtain_gas = db.Column('Hrms_Curtain_Gas', db.Float(10), nullable=False)
    hrms_ionisation = db.Column('Hrms_Ionisation', db.Float(10), nullable=False)
    hrms_voltage = db.Column('Hrms_Voltage', db.Float(10), nullable=False)
    hrms_polarity = db.Column('Hrms_Polarity', db.Float(10), nullable=False)
    hrms_source = db.Column('Hrms_Source', db.Float(10), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}', '{self.system_brand}')"

class Analytical_Column(db.Model, UserMixin):
    __tablename__ = 'analytical_column'
    id = db.Column('Column_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column('User_ID', db.Integer, unique=True, nullable=False)
    column_phase = db.Column('Column_Phase', db.String(255), nullable=False)
    column_praticle_size = db.Column('Column_Particle_Size', db.String(255), nullable=False)
    column_length = db.Column('Column_Length', db.String(255), nullable=False)
    column_pore_size = db.Column('Column_Pore_Size', db.String(255), nullable=False)
    column_inner_diameter = db.Column('Column_Inner_Diameter', db.String(255), nullable=False)
    column_brand = db.Column('Column_Brand', db.String(255), nullable=False)
    column_model = db.Column('Column_Model', db.String(255), nullable=False)
    column_time_last_used = db.Column('Column_Time_Last_Used', db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.id}', '{self.column_time_last_used}')"

class Chromatographic_Condition(db.Model, UserMixin):
    __tablename__ = 'chromatographic_condition'
    id = db.Column('Acqui_Chrom_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    column_id = db.Column('Column_ID', db.Integer, unique=True, nullable=False)
    sample_injection_volume = db.Column('Sample_Injection_Volume', db.String(255), nullable=False)
    mobile_phase_a = db.Column('Mobile_Phase_A', db.Float(10), nullable=False)
    mobile_phase_b = db.Column('Mobile_Phase_B', db.Float(10), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.id}', '{self.sample_injection_volume}')"

class Chrom_Time(db.Model, UserMixin):
    __tablename__ = 'chrom_time'
    id = db.Column('Chrom_Events_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    acqui_chrom_id = db.Column('Acqui_Chrom_ID', db.Integer, unique=True, nullable=False)
    event_stage = db.Column('Event_Stage', db.String(255), nullable=False)
    flow_rate = db.Column('Flow_Rate', db.Float(10), nullable=False)
    time = db.Column('Time', db.DateTime, nullable=False, default=datetime.utcnow)
    gradient_a_or_b = db.Column('Gradient_A/B', db.Float(10), nullable=False)
    a_or_b = db.Column('A/B', db.String(2), nullable=False)
    oven_temp = db.Column('Oven_Temp', db.Float(10), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.id}', '{self.event_stage}')"

class Lc_System(db.Model, UserMixin):
    __tablename__ = 'lc_system'
    id = db.Column('LC_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    acqui_chrom_id = db.Column('Acqui_Chrom_ID', db.Integer, unique=True, nullable=False)
    user_id = db.Column('User_ID', db.Integer, unique=True, nullable=False)
    system_brand = db.Column('System_Brand', db.String(255), nullable=False)
    system_model = db.Column('System_Model', db.String(255), nullable=False)
    system_chrom_class = db.Column('System_Chrom_Class',db.String(255), nullable=False)
    system_component_type = db.Column('System_Component_Type', db.String(255), nullable=False)
    system_time_last_used = db.Column('System_Time_Last_Used', db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.id}', '{self.System_time_last_used}')"

class Ms_System(db.Model, UserMixin):
    __tablename__ = 'ms_system'
    id = db.Column('Hrms_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    acqui_hrms_id = db.Column('Acqui_Hrms_ID', db.Integer, unique=True, nullable=False)
    system_class = db.Column('System_Class', db.String(255), nullable=False)
    system_model = db.Column('System_Model', db.String(255), nullable=False)
    system_brand = db.Column('System_Brand',db.String(255), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}', '{self.system_brand}')"

class Reference_Library(db.Model, UserMixin):
    __tablename__ = 'reference_library'
    id = db.Column('Library_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    reference_path = db.Column('Reference_Path', db.String(255), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.id}', '{self.reference_path}')"

class Results(db.Model, UserMixin):
    __tablename__ = 'results'
    id = db.Column('Result_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    d_set_id = db.Column('D_Set_ID', db.Integer, unique=True, nullable=False)
    column_id = db.Column('Column_ID', db.Integer, unique=True, nullable=False)
    lc_id = db.Column('LC_ID', db.Integer, unique=True, nullable=False)
    hrms_id = db.Column('Hrms_ID', db.Integer, unique=True, nullable=False)
    sample_id = db.Column('Sample_ID', db.Integer, unique=True, nullable=False)
    deconv_file_path = db.Column('Deconv_File_Path', db.String(255), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}', '{self.d_set_id}', '{self.column_id}', '{self.lc_id}', '{self.hrms_id}', '{self.sample_id}', '{self.deconv_file_path}')"

class Sample_Information(db.Model, UserMixin):
    __tablename__ = 'sample_information'
    id = db.Column('Sample_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column('User_ID', db.Integer, unique=True, nullable=False)
    sample_raw_hrms_file_path = db.Column('Sample_Raw_Hrms_File_Path', db.String(255), nullable=False, default='path one')
    sample_targets_file_path = db.Column('Sample_Targets_File_Path', db.String(255), nullable=False, default='path two')
    sample_matrix = db.Column('Sample_Matrix', db.String(255), nullable=False, default='default sample matrix')
    sample_private = db.Column('Sample_Private',db.String(2), nullable=False)
    sample_is_processed = db.Column('Sample_Is_Processed',db.String(2), nullable=False, default='Y')
    sample_type = db.Column('Sample_Type',db.String(255), nullable=False)
    sample_job_number = db.Column('Sample_Job_Number',db.String(255), nullable=False)
    sample_city = db.Column('Sample_City',db.String(255), nullable=False)
    sample_date = db.Column('Sample_Date',db.DateTime, nullable=False, default= datetime.utcnow)
    sample_country = db.Column('Sample_Country',db.String(255), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}', '{self.sample_is_processed}')"

class Sample_Location(db.Model, UserMixin):
    __tablename__ = 'sample_location'
    id = db.Column('Location_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    sample_id = db.Column('Sample_ID', db.Integer, unique=True, nullable=False)
    location_longitude = db.Column('Location_Longitude', db.Float(10), nullable=False)
    location_altitude = db.Column('Location_Altitude', db.Float(10), nullable=False)
    location_latitude = db.Column('Location_Latitude', db.Float(10), nullable=False)
    location_datum = db.Column('Location_Datum',db.Float(10), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}', '{self.location_longitude}', '{self.location_altitude}', '{self.location_latitude}')"

class Search_Results(db.Model, UserMixin):
    __tablename__ = 'search_results'
    id = db.Column('Search_Results_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    candidate_name = db.Column('Candidate_Name', db.String(255), nullable=False)
    confidence_score_global = db.Column('Confidence_Score_Global', db.String(255), nullable=False)
    confidence_score = db.Column('Confidence_Score', db.String(255), nullable=False)
    sample_id = db.Column('Sample_ID', db.Integer, unique=True, nullable=False)
    retention_time = db.Column('Retention_Time', db.DateTime, nullable=False)
    m_or_z = db.Column('M/Z',db.String(2), nullable=False)
    is_smile = db.Column('Is_Smile',db.String(2), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}', '{self.candidate_name}', '{self.confidence_score_global}', '{self.confidence_score}')"

class Threshold_Setting(db.Model, UserMixin):
    __tablename__ = 'threshold_setting'
    id = db.Column('D_Set_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    mas_w = db.Column('Mas_W', db.String(255), nullable=False)
    min_int = db.Column('Min_Int', db.String(255), nullable=False)
    retention_window = db.Column('Retention_Window', db.String(255), nullable=False)
    r_min = db.Column('R_Min', db.String(255), nullable=False)
    p_max = db.Column('P_Max', db.String(255), nullable=False)
    retention_time_tollerance = db.Column('Retention_Time_Tollerance',db.String(255), nullable=False)
    ms_p_w = db.Column('Ms_P_W',db.String(255), nullable=False)
    mass_tol = db.Column('Mass_Tol',db.String(255), nullable=False)
    mass_window = db.Column('Mass_Window',db.String(255), nullable=False)
    signal_to_noise = db.Column('Signal_To_Noise',db.String(255), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}', '{self.mas_w}', '{self.min_int}', '{self.retention_window}')"


