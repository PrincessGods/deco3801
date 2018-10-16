from flask import render_template, url_for, redirect, request, Blueprint, flash
from application.hams.forms import SelectMethodForm, AcquisitionForm, DeconvLibrarySearch, LibrarySearch, ImportDeconv, AlgorithmnForm
from application.models import User
from application import db
from application.hams.utils import save_datafile, LibrarySearch_Al, DeconvLibrarySearch_Al, ImportDeconv_Al
from flask_login import login_required, current_user

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

@hams.route("/manageJobs")
@login_required
def manageJobs():
    return render_template('manageJobs.html', title = "HAMS")

@hams.route("/chooseMethod", methods=['GET', 'POST'])
@login_required
def chooseMethod():
    form = SelectMethodForm()
    methodList = getMethodList()
    if form.validate_on_submit():
        chosenMethod = form.methods.data
        return redirect(url_for('hams.acquisition', chosenMethod = chosenMethod))
        
    return render_template('chooseMethod.html', title = "HAMS", form = form,
                             details = details, methods = methodList)

@hams.route("/acquisition/<chosenMethod>", methods=['GET', 'POST'])
@login_required
def acquisition(chosenMethod):
    if chosenMethod == 'LibrarySearch':
        form = LibrarySearch()
    elif chosenMethod == 'ImportDeconv':
        form = ImportDeconv()
    else:
        form = DeconvLibrarySearch()

    if form.validate_on_submit():
        if chosenMethod == 'ImportDeconv':
            xlsxFile = save_datafile(form.xlsxFile, current_user.username)
            #current_user.Target = xlsxFile

            VANFileLow = save_datafile(form.VANFileLow, current_user.username)
            #current_user.Low_Energy = VANFileLow
        
            VANFileHigh = save_datafile(form.VANFileHigh, current_user.username)
            #current_user.High_Energy = VANFileHigh

        elif chosenMethod == 'LibrarySearch':
            txtFile = save_datafile(form.txtFile, current_user.username)
            #current_user.Spectra = txtFile

        else:
            xlsxFile = save_datafile(form.xlsxFile, current_user.username)
            #current_user.Target = xlsxFile

            VANFileLow = save_datafile(form.VANFileLow, current_user.username)
            #current_user.Low_Energy = VANFileLow
        
            VANFileHigh = save_datafile(form.VANFileHigh, current_user.username)
            #current_user.High_Energy = VANFileHigh

            txtFile = save_datafile(form.txtFile, current_user.username)
            #current_user.Spectra = txtFile

        return redirect(url_for('hams.saveJob', chosenMethod = chosenMethod))
    return render_template('acquisition.html', title = "HAMS", form = form, method = chosenMethod) 

@hams.route("/saveJob/<chosenMethod>", methods=['GET', 'POST'])
@login_required
def saveJob(chosenMethod):
    form = AlgorithmnForm()
    if form.validate_on_submit():
        if chosenMethod == 'ImportDeconv':
            ImportDeconv_Al()
        elif chosenMethod == 'LibrarySearch':
            LibrarySearch_Al("ESI", "POSITIVE")
        else:
            DeconvLibrarySearch_Al()

        return redirect(url_for('users.profile'))
    return render_template('saveJob.html', title = "HAMS", form = form)
