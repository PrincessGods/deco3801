from flask import render_template, request, Blueprint, flash, redirect, url_for
from application.models import User, Sample_Information, Sample_Location, Search_Results
from application import db, bcrypt
from application.main.forms import HomeSearchForm
from flask_login import current_user

main = Blueprint('main', __name__)

@main.route("/")

@main.route("/home", methods=['GET', 'POST'])
def home():
    form = HomeSearchForm()
    user_icon = getUserIcon()
    if form.validate_on_submit():
        c_name = form.search.data
        return redirect(url_for('main.search', name=c_name))
    return render_template('index.html', title = "QAEHS", form = form, icon = user_icon)

@main.route("/search/<name>", methods=['GET', 'POST'])
def search(name):
    form = HomeSearchForm()
    user_icon = getUserIcon()
    samples = Sample_Information.query.filter_by(sample_type = name).all()
    return render_template('chemical_search.html', title = "Search Result", 
                            form = form, icon = user_icon, samples = samples)

@main.route("/searchDetails/<id>", methods=['GET', 'POST'])
def searchDetails(id):
    form = HomeSearchForm()
    user_icon = getUserIcon()
    sample = Sample_Information.query.filter_by(id = id).first()
    location = Sample_Location.query.filter_by(sample_id = id).first()
    return render_template('search_result_detials.html', title = "Search Result Details", 
                            form = form, icon = user_icon, sample = sample,
                            location = location)

def getUserIcon():
    if current_user.is_authenticated:
        user_icon = url_for('static', filename='imgs/' + current_user.user_icon)
        return user_icon
    

