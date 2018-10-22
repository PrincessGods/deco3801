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
        projectpath = request.form['projectFilepath']
        return redirect(projectpath)
    return render_template('forum.html', title='Forum', 
                            form=form, icon = user_icon, 
                            posts = posts)

@forum.route("/forum/post", methods=['GET', 'POST'])
def viewpost_post():
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
        return redirect(url_for('forum.viewpost_post'))
    return render_template('forum.html', title='Forum', 
                            form=form, icon = user_icon, 
                            posts = posts)

@forum.route("/forum/<postID>", methods=['GET', 'POST'])
def viewpostDetails(postID):
    form = PostForm()
    user_icon = getUserIcon()
    post = Post.query.filter_by(post_id = postID).first()
    print(post)
    # if form.validate_on_submit():
    #     post = Post(
    #         title = form.title.data,
    #         contents = form.content.data,
    #         owner = current_user.id
    #     )

    #     db.session.add(post)
    #     db.session.commit()

    #     return redirect(url_for('forum.viewpostDetails'))
    return render_template('post_details.html', title='Post Details', 
                            form=form, icon = user_icon, 
                            post = post)