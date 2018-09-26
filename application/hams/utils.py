import secrets
import os
import boto3
from flask import url_for, current_app, request

def save_datafile(form_datafile, user):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_datafile.data.filename)
    fn = random_hex + f_ext
    s3 = boto3.client('s3')
    bucket_name = 'deco3801'
    dir_n = user + '/unprocessed/test/Other/' + fn

    if form_datafile.label == 'Target':
        dir_n = user + '/unprocessed/test/Target/' + fn
    elif form_datafile.label == 'HRMS Data (Low Energy)':
        dir_n = user + '/unprocessed/test/Low Energy/' + fn
    elif form_datafile.label == 'HRMS Data (High Energy)':
        dir_n = user + '/unprocessed/test/High Energy/' + fn
    else:
        user + '/unprocessed/test/User Spectra/' + fn

    s3.put_object(Bucket=bucket_name, Key=dir_n, Body=form_datafile.data)

    """ if form_datafile.label == 'Target':
        new_path = (current_app.root_path +
                '/static/data/' + user + 
                '/unprocessed/test/Target/')
    elif form_datafile.label == 'HRMS Data (Low Energy)':
        new_path = (current_app.root_path +
                '/static/data/' + user + 
                '/unprocessed/test/Low Energy/')
    elif form_datafile.label == 'HRMS Data (High Energy)':
        new_path = (current_app.root_path +
                '/static/data/' + user + 
                '/unprocessed/test/High Energy/')
    else:
        new_path = (current_app.root_path +
                '/static/data/' + user + 
                '/unprocessed/test/User Spectra/')
    
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    if form_datafile.label == 'Target':
        file_path = os.path.join(current_app.root_path,
                            'static/data/', user,
                            'unprocessed/test/Target/', fn)

    elif form_datafile.label == 'HRMS Data (Low Energy)':
        file_path = os.path.join(current_app.root_path,
                            'static/data/', user,
                            'unprocessed/test/Low Energy/', fn)

    elif form_datafile.label == 'HRMS Data (High Energy)':
        file_path = os.path.join(current_app.root_path,
                            'static/data/', user,
                            'unprocessed/test/High Energy/', fn)

    else:
        file_path = os.path.join(current_app.root_path,
                            'static/data/', user,
                            'unprocessed/test/User Spectra/', fn)

    form_datafile.data.save(file_path) """

    return fn