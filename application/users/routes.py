from flask import render_template, url_for, flash, redirect, request, Blueprint
from application import db, bcrypt
from application.users.forms import (RegistrationForm, LoginForm, UpdateProfileForm,
                                RequestResetForm, ResetPasswordForm)
from application.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from application.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users.login'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
                            form.password.data).decode('utf-8')
        user = User(username = form.username.data, 
                        email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()

        ##flash(f'Your account has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Register', 
                            form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter((User.email==form.email.data) | 
                                (User.username==form.email.data)).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            ##flash('You have been logged in!', 'success')
            if next_page:
                return redirect(next_page)
            else: 
                return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check Username/Email and Password', 'danger')
    return render_template('login.html', title='Login', 
                            form=form)

@users.route("/logout")
def logout():
    logout_user()
    ##this_page = request.args.get('')
    return redirect(url_for('main.home'))

@users.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.u_icon = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    u_icon = url_for('static', filename='imgs/' + current_user.u_icon)
    return render_template('profile.html', title = "My Profile", 
                            icon = u_icon, form = form)

@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instrutions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', 
                            title='Reset Password', form=form)

@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
                            form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()

        flash(f'Your password has been updated!', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', 
                            title='Reset Password', form=form)