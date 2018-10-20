from flask import render_template, url_for, redirect, request, Blueprint, flash
from application.hams.forms import SelectMethodForm, AcquisitionForm, DeconvLibrarySearch, LibrarySearch, ImportDeconv, AlgorithmnForm
from application.models import User, Acquisition_Hrms, Ms_System, Sample_Information, Sample_Location, Analytical_Column, Chromatographic_Condition, Chrom_Time, Lc_System, Threshold_Setting
from application import db
from application.hams.utils import save_datafile_L, save_datafile_D, save_datafile_DL
from flask_login import login_required, current_user
import secrets

hams = Blueprint('hams', __name__)

details = [
    {
        'title' : 'Library Search',
        'description' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
    },
    {
        'title' : 'Import Deconv',
        'description' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
    },
    {
        'title' : 'Deconv & Library Search',
        'description' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
    }
]

def getMethodList():
    methodList = []
    for method in SelectMethodForm().methods:
        methodList.append(method)
    return methodList

def getUserIcon():
    if current_user.is_authenticated:
        user_icon = url_for('static', filename='imgs/' + current_user.user_icon)
        return user_icon

def getJobID():
    random_hex = secrets.token_hex(8)
    while Sample_Information.query.filter_by(sample_job_number=random_hex).first():
        random_hex = secrets.token_hex(8)

    return random_hex

@hams.route("/manageJobs")
@login_required
def manageJobs():
    user_icon = getUserIcon()
    return render_template('manageJobs.html',icon = user_icon, title = "HAMS")

@hams.route("/chooseMethod", methods=['GET', 'POST'])
@login_required
def chooseMethod():
    form = SelectMethodForm()
    methodList = getMethodList()
    user_icon = getUserIcon()
    if form.validate_on_submit():
        chosenMethod = form.methods.data
        return redirect(url_for('hams.acquisition', chosenMethod = chosenMethod))
        
    return render_template('chooseMethod.html', title = "HAMS", form = form,
                             details = details, methods = methodList, icon = user_icon)

@hams.route("/acquisition/<chosenMethod>", methods=['GET', 'POST'])
@login_required
def acquisition(chosenMethod):
    user_icon = getUserIcon()

    if chosenMethod == 'LibrarySearch':
        form = LibrarySearch()
    elif chosenMethod == 'ImportDeconv':
        form = ImportDeconv()
    else:
        form = DeconvLibrarySearch()

    if form.validate_on_submit():
        j_id = getJobID()
        
        if chosenMethod == 'ImportDeconv':
            fileList = []
            fileList.append(form.xlsxFile)
            fileList.append(form.VANFileLow)
            fileList.append(form.VANFileHigh)

            d_set = []
            d_set.append(form.Max_W.data)
            d_set.append(form.Min_Int.data)
            d_set.append(form.Retention_Window.data)
            d_set.append(form.R_Min.data)
            d_set.append(form.P_Max.data)
            d_set.append(form.Retention_Time_Tollerance.data)
            d_set.append(form.Ms_P_W.data)
            d_set.append(form.Mass_Tol.data)
            d_set.append(form.Mass_Window.data)
            d_set.append(form.Signal_to_Noise.data)

            save_datafile_D(fileList, current_user.user_email, j_id, d_set)

        elif chosenMethod == 'LibrarySearch':
            #source =
            #mode = 

            save_datafile_L(form.txtFile, current_user.user_email, j_id, 'ESI', 'POSITIVE')

        else:
            fileList = []
            fileList.append(form.xlsxFile)
            fileList.append(form.VANFileLow)
            fileList.append(form.VANFileHigh)
            fileList.append(form.txtFile)

            d_set = []
            d_set.append(float(form.Max_W.data))
            d_set.append(float(form.Min_Int.data))
            d_set.append(float(form.Retention_Window.data))
            d_set.append(float(form.R_Min.data))
            d_set.append(float(form.P_Max.data))
            d_set.append(float(form.Retention_Time_Tollerance.data))
            d_set.append(float(form.Ms_P_W.data))
            d_set.append(float(form.Mass_Tol.data))
            d_set.append(float(form.Mass_Window.data))
            d_set.append(float(form.Signal_to_Noise.data))

            #source =
            #mode = 

            save_datafile_DL(fileList, current_user.user_email, j_id, d_set, 'ESI', 'POSITIVE')

        #Main tables
        if chosenMethod == 'LibrarySearch' or chosenMethod == 'DeconvLibrarySearch':
            Threshold_Setting = Threshold_Setting(
                mas_w = form.Max_W.data, 
                min_int = form.Min_Int.data, 
                retention_window = form.Retention_Window.data,
                r_min = form.R_Min.data,
                p_max = form.P_Max.data,
                retention_time_tollerance = form.Retention_Time_Tollerance.data,
                ms_p_w = form.Ms_P_W.data,
                mass_tol = form.Mass_Tol.data,
                mass_window = form.Mass_Window.data,
                signal_to_noise = form.Signal_to_Noise.data
            )

            db.session.add(Threshold_Setting)

        acquisition_hrms = Acquisition_Hrms(hrms_mode = form.hrms_mode.data, 
                    hrms_source_gas1 = form.hrms_source_gas1.data, 
                    hrms_source_gas2 = form.hrms_source_gas2.data,
                    hrms_curtain_gas = form.hrms_curtain_gas.data,
                    hrms_ionisation = form.hrms_ionisation.data,
                    hrms_voltage = form.hrms_voltage.data,
                    hrms_polarity = form.hrms_polarity.data,
                    hrms_source = form.hrms_source.data)

        sample_information = Sample_Information(user_id = getattr(current_user,'id'), 
                    sample_private = form.sample_private.data, 
                    sample_type = form.sample_type.data,
                    sample_city = form.sample_city.data,
                    sample_job_number = getJobID(),
                    sample_country  = form.sample_country.data)

        analytical_column = Analytical_Column(user_id = getattr(current_user,'id'), 
                    column_phase = form.column_phase.data, 
                    column_praticle_size = form.column_particle_size.data,
                    column_length = form.column_length.data,
                    column_pore_size  = form.column_pore_size.data,
                    column_inner_diameter  = form.column_inner_diameter.data,
                    column_brand  = form.column_brand.data,
                    column_model  = form.column_model.data)

        db.session.add(acquisition_hrms)
        db.session.add(sample_information)
        db.session.add(analytical_column)
        db.session.commit()

        #Sub tables
        ms_system = Ms_System(acqui_hrms_id = getattr(acquisition_hrms,'id'),
                    system_class = form.hrms_system_class.data,
                    system_model = form.hrms_system_model.data,
                    system_brand = form.hrms_system_brand.data)

        sample_location = Sample_Location(sample_id = getattr(sample_information,'id'),
                    location_longitude = form.sample_location_longitude.data,
                    location_altitude = form.sample_location_altitude.data,
                    location_latitude = form.sample_location_latitude.data,
                    location_datum = form.sample_location_datum.data)

        chromatographic_condition = Chromatographic_Condition(column_id = getattr(analytical_column,'id'), 
                    sample_injection_volume = form.chrom_sample_injection_volume.data, 
                    mobile_phase_a = form.chrom_mobile_phase_a.data,
                    mobile_phase_b = form.chrom_mobile_phase_b.data)

        db.session.add(ms_system)
        db.session.add(sample_location)
        db.session.add(chromatographic_condition)
        db.session.commit()

        chrom_time = Chrom_Time(acqui_chrom_id = getattr(chromatographic_condition,'id'), 
                    event_stage = form.chrom_event_stage.data, 
                    flow_rate = form.chrom_flow_rate.data,
                    gradient_a_or_b = form.chrom_gradient_a_or_b.data,
                    a_or_b = form.chrom_a_or_b.data,
                    oven_temp = form.chrom_oven_temperature.data)

        lc_system = Lc_System(acqui_chrom_id = getattr(chromatographic_condition,'id'),
                    user_id = getattr(current_user,'id'),
                    system_brand = form.chrom_system_brand.data, 
                    system_model = form.chrom_system_model.data,
                    system_chrom_class = form.chrom_system_class.data,
                    system_component_type = form.chrom_component_type.data)

        db.session.add(chrom_time)
        db.session.add(lc_system)

        db.session.commit()

        return redirect(url_for('hams.saveJob', chosenMethod = chosenMethod))
    return render_template('acquisition.html', title = "HAMS", form = form, method = chosenMethod, icon = user_icon) 

@hams.route("/saveJob/<chosenMethod>", methods=['GET', 'POST'])
@login_required
def saveJob(chosenMethod):
    form = AlgorithmnForm()
    user_icon = getUserIcon()
    j_id = getJobID()
    if form.validate_on_submit():

        return redirect(url_for('users.profile'))
    return render_template('saveJob.html', title = "HAMS", form = form, icon = user_icon)
