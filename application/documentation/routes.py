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

@documentation.route("/downloadPaper/<file_id>", methods=['GET', 'POST'])
def download_paper(file_id):
    file_path = Paper.query.filter_by(paper_id = file_id).first()
    url = DownloadPdf(file_path)
    print(url)
    return redirect(url)