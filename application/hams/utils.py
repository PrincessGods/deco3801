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

    if form_datafile.id == 'xlsxFile':
        dir_n = user + '/unprocessed/test/Target/' + fn
    elif form_datafile.id == 'VANFileLow':
        dir_n = user + '/unprocessed/test/Low Energy/' + fn
    elif form_datafile.id == 'VANFileHigh':
        dir_n = user + '/unprocessed/test/High Energy/' + fn
    else:
        dir_n = user + '/unprocessed/test/User Spectra/' + fn

    s3.put_object(Bucket=bucket_name, Key=dir_n, Body=form_datafile.data)
    
    return fn