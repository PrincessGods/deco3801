from flask import render_template, url_for, redirect, request, Blueprint, flash
from application.hams.forms import SelectMethodForm, AcquisitionForm
from application.models import User
from application import db
from flask_login import login_required
##from application.hams.utils import 

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
def manageJobs():
    return render_template('manageJobs.html', title = "HAMS")

@hams.route("/chooseMethod", methods=['GET', 'POST'])
def chooseMethod():
    form = SelectMethodForm()
    methodList = getMethodList()
    if request.method == 'POST':
        chosenMethod = form.methods.data
        return redirect(url_for('hams.acquisition', chosenMethod = chosenMethod))
        
    return render_template('chooseMethod.html', title = "HAMS", form = form,
                             details = details, methods = methodList)

@hams.route("/acquisition/<chosenMethod>", methods=['GET', 'POST'])
def acquisition(chosenMethod):
    form = AcquisitionForm()
    if request.method == 'POST':
        return redirect(url_for('hams.saveJob'))
    #else:
        #flash('Save Unsuccessful. Please complete the form', 'info')
    return render_template('acquisition.html', title = "HAMS", form = form, method = chosenMethod) 

@hams.route("/saveJob", methods=['GET', 'POST'])
def saveJob():
    return render_template('saveJob.html', title = "HAMS")

##@hams.route("/createNewJob")