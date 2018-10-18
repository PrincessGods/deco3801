from flask import render_template, request, Blueprint, flash, redirect, url_for
from application.models import Post
from application.main.forms import HomeSearchForm
from flask_login import current_user

main = Blueprint('main', __name__)

@main.route("/")

@main.route("/home", methods=['GET', 'POST'])
def home():
    form = HomeSearchForm()
    user_icon = getUserIcon()
    if form.validate_on_submit():
        return redirect(url_for('users.profile'))
    return render_template('index.html', title = "QAEHS", form = form, icon = user_icon)

@main.route("/search/", methods=['GET', 'POST'])
def search():
    form = HomeSearchForm()
    if form.validate_on_submit():
        return redirect(url_for('users.profile'))
    #return render_template('index.html', title = "QAEHS", form = form)
    #if form.validate_on_submit():
    #    return redirect(url_for('users.profile'))
    #else:
    #    return redirect(url_for('users.login'))

def getUserIcon():
    if current_user.is_authenticated:
        user_icon = url_for('static', filename='imgs/' + current_user.user_icon)
        return user_icon
    

