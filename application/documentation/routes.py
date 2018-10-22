from flask import render_template, url_for, flash, redirect, request, Blueprint
from application import db, bcrypt
from application.documentation.forms import PaperForm, PaperSearchForm
from application.models import User, Post, Paper
from flask_login import login_user, current_user, logout_user, login_required

documentation = Blueprint('documentation', __name__)

def getUserIcon():
    if current_user.is_authenticated:
        user_icon = url_for('static', filename='imgs/' + current_user.user_icon)
        return user_icon

@documentation.route("/paper", methods=['GET', 'POST'])
def viewpapers():
    form = PaperForm()
    searchform = PaperSearchForm()
    user_icon = getUserIcon()
    papers = Paper.query.all()
    if form.validate_on_submit():
        projectpath = request.form['projectFilepath']
        return redirect(projectpath)
    return render_template('paper.html', title='Paper', 
                            form=form, icon = user_icon, 
                            papers = papers, searchform = searchform)