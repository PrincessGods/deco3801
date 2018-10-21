from flask import render_template, url_for, flash, redirect, request, Blueprint
from application import db, bcrypt
from application.forum.forms import PostForm
from application.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

forum = Blueprint('forum', __name__)

def getUserIcon():
    if current_user.is_authenticated:
        user_icon = url_for('static', filename='imgs/' + current_user.user_icon)
        return user_icon

@forum.route("/forum", methods=['GET', 'POST'])
def viewpost():
    form = PostForm()
    user_icon = getUserIcon()
    posts = Post.query.all()
    if form.validate_on_submit():
        post = Post(
            title = form.title.data,
            contents = form.content.data,
            owner = current_user.id
        )

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('forum.viewpost'))
    return render_template('forum.html', title='Forum', 
                            form=form, icon = user_icon, 
                            posts = posts)