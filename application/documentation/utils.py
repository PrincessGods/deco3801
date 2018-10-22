import secrets
import os
import boto3
import LibrarySearch_v1
import ImportDeconv_v1
import DeconvLibrarySearch_v1
from os.path import join
from flask import url_for, current_app, request
import subprocess

def save_pdf(form_datafile, user):
    f_name, f_ext = os.path.splitext(form_datafile.data.filename)
    fn = f_name + f_ext

    command = 'mkdir -p /home/ubuntu/deco3801/application/static/paper/' + user
    subprocess.call(command, shell=True)

    file_path = os.path.join(current_app.root_path,
                            'static/paper/', user, fn)
    form_datafile.data.save(file_path)
    fn_path = 'static/paper/' + user + '/' + fn
    
    return fn_path

def DownloadPdf(file_path):
    url = join('http://', file_path)
    return url