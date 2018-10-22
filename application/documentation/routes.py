from flask import render_template, url_for, flash, redirect, request, Blueprint
from application import db, bcrypt
from application.documentation.forms import PaperForm, PaperSearchForm
from application.documentation.utils import save_pdf, DownloadPdf
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
        path = save_pdf(form.paper_file, current_user.user_email)
        print(path)
        paper = Paper(
            title = form.title.data,
            path = path,
            owner = current_user.id,
            paper_author = form.paper_author.data
        )
        db.session.add(paper)
        db.session.commit()
        return redirect(url_for('documentation.viewpapers'))
    return render_template('paper.html', title='Paper', 
                            form=form, icon = user_icon, 
                            papers = papers, searchform = searchform)

@documentation.route("/download/<file_path>", methods=['GET', 'POST'])
def download(file_path):
    url = join('http://', request.host, file_path)
    print(url)
    return redirect(url)