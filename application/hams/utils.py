import secrets
import os
import boto3
from flask import url_for, current_app

def save_Target(form_Target, user):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_Target.filename)
    fn = random_hex + f_ext
    s3 = boto3.client('s3')
    dir_n = user + '/unprocessed/test/Target/' + fn
    bucket_name = 'deco3801'

    s3.upload_file(dir_n, bucket_name, fn)

    # new_path = (current_app.root_path +
    #             '/static/data/' + user + 
    #             '/unprocessed/test/Target/')
    # if not os.path.exists(new_path):
    #     os.makedirs(new_path)

    # file_path = os.path.join(current_app.root_path,
    #                         'static/data/', user,
    #                         'unprocessed/test/Target/', fn)
    # form_Target.save(file_path)

    return fn

def save_Low_Energy(form_Low_Energy, user):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_Low_Energy.filename)
    fn = random_hex + f_ext
    s3 = boto3.client('s3')
    dir_n = user + '/unprocessed/test/Low Energy/' + fn
    bucket_name = 'deco3801'

    s3.upload_file(dir_n, bucket_name, fn)

    # new_path = (current_app.root_path +
    #             '/static/data/' + user + 
    #             '/unprocessed/test/Low Energy/')
    # if not os.path.exists(new_path):
    #     os.makedirs(new_path)

    # file_path = os.path.join(current_app.root_path,
    #                         'static/data/', user,
    #                         'unprocessed/test/Low Energy/', fn)
    # form_Low_Energy.save(file_path)

    return fn

def save_High_Energy(form_High_Energy, user):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_High_Energy.filename)
    fn = random_hex + f_ext
    s3 = boto3.client('s3')
    dir_n = user + '/unprocessed/test/High Energy/' + fn
    bucket_name = 'deco3801'

    s3.upload_file(dir_n, bucket_name, fn)
    # new_path = (current_app.root_path +
    #             '/static/data/' + user + 
    #             '/unprocessed/test/High Energy/')
    # if not os.path.exists(new_path):
    #     os.makedirs(new_path)

    # file_path = os.path.join(current_app.root_path,
    #             'static/data/', user,
    #             'unprocessed/test/High Energy/', fn)
    # form_High_Energy.save(file_path)

    return fn

def save_Spectra(form_Spectra, user):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_Spectra.filename)
    fn = random_hex + f_ext
    s3 = boto3.client('s3')
    dir_n = user + '/unprocessed/test/User Spectra/' + fn
    bucket_name = 'deco3801'

    s3.upload_file(dir_n, bucket_name, fn)
    # new_path = (current_app.root_path +
    #             '/static/data/' + user + 
    #             '/unprocessed/test/User Spectra/')
    # if not os.path.exists(new_path):
    #     os.makedirs(new_path)

    # file_path = os.path.join(current_app.root_path,
    #             'static/data/', user,
    #             'unprocessed/test/User Spectra/', fn)
    # form_Spectra.save(file_path)

    return fn
