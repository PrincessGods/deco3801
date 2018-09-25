from flask import render_template, request, Blueprint, flash, redirect, url_for
from application.models import Post
from application.main.forms import HomeSearchForm

main = Blueprint('main', __name__)

@main.route("/")

@main.route("/home", methods=['GET', 'POST'])
def home():
    form = HomeSearchForm()
    if form.validate_on_submit():
        return redirect(url_for('users.profile'))
    return render_template('index.html', title = "QAEHS", form = form)

@main.route("/search/", methods=['GET', 'POST'])
def search():
    form = HomeSearchForm()
    if form.validate_on_submit():
        return redirect(url_for('users.profile'))
    return render_template('index.html', title = "QAEHS", form = form)
    #if form.validate_on_submit():
    #    return redirect(url_for('users.profile'))
    #else:
    #    return redirect(url_for('users.login'))
    

