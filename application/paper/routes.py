from flask import render_template, url_for, flash, redirect, request, Blueprint
from application import db, bcrypt
from application.paper.forms import PostForm
from application.models import User, Post, Paper
from flask_login import login_user, current_user, logout_user, login_required

paper = Blueprint('paper', __name__)

def getUserIcon():
    if current_user.is_authenticated:
        user_icon = url_for('static', filename='imgs/' + current_user.user_icon)
        return user_icon

@paper.route("/paper", methods=['GET', 'POST'])
def viewpapers():
    form = PostForm()
    user_icon = getUserIcon()
    papers = Paper.query.all()
    if form.validate_on_submit():
        projectpath = request.form['projectFilepath']
        return redirect(projectpath)
    return render_template('paper.html', title='Paper', 
                            form=form, icon = user_icon, 
                            papers = paper)