import secrets
import os
import boto3
import LibrarySearch_v1
from os.path import join
from flask import url_for, current_app, request

def save_datafile(form_datafile, user):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_datafile.data.filename)
    fn = "Other" + f_ext
    s3 = boto3.client('s3', aws_access_key_id='', 
                        aws_secret_access_key='')
    bucket_name = 'deco3801'
    dir_n = user + '/unprocessed/test/Other/' + fn

    if form_datafile.id == 'xlsxFile':
        fn = "Target" + f_ext
        dir_n = user + '/unprocessed/test/Target/' + fn
    elif form_datafile.id == 'VANFileLow':
        fn = "Low_Energy" + f_ext
        dir_n = user + '/unprocessed/test/Low Energy/' + fn
    elif form_datafile.id == 'VANFileHigh':
        fn = "High_Energy" + f_ext
        dir_n = user + '/unprocessed/test/High Energy/' + fn
    else:
        fn = "User_Spectra" + f_ext
        dir_n = user + '/unprocessed/test/User Spectra/' + fn

    s3.put_object(Bucket=bucket_name, Key=dir_n, Body=form_datafile.data)

    # if form_datafile.id == 'xlsxFile':
    #     new_path = (current_app.root_path +
    #             '/static/data/' + user + 
    #             '/unprocessed/test/Target/')
    # elif form_datafile.id == 'VANFileLow':
    #     new_path = (current_app.root_path +
    #             '/static/data/' + user + 
    #             '/unprocessed/test/Low Energy/')
    # elif form_datafile.id == 'VANFileHigh':
    #     new_path = (current_app.root_path +
    #             '/static/data/' + user + 
    #             '/unprocessed/test/High Energy/')
    # else:
    #     new_path = (current_app.root_path +
    #             '/static/data/' + user + 
    #             '/unprocessed/test/User Spectra/')
    
    # if not os.path.exists(new_path):
    #     os.makedirs(new_path)

    # if form_datafile.id == 'xlsxFile':
    #     file_path = os.path.join(current_app.root_path,
    #                         'static/data/', user,
    #                         'unprocessed/test/Target/', fn)

    # elif form_datafile.id == 'VANFileLow':
    #     file_path = os.path.join(current_app.root_path,
    #                         'static/data/', user,
    #                         'unprocessed/test/Low Energy/', fn)

    # elif form_datafile.id == 'VANFileHigh':
    #     file_path = os.path.join(current_app.root_path,
    #                         'static/data/', user,
    #                         'unprocessed/test/High Energy/', fn)

    # else:
    #     file_path = os.path.join(current_app.root_path,
    #                         'static/data/', user,
    #                         'unprocessed/test/User Spectra/', fn)

    # form_datafile.data.save(file_path)
    
    return fn

def DeconvLibrarySearch_Al():
    random_hex = secrets.token_hex(8)

def ImportDeconv_Al():
    random_hex = secrets.token_hex(8)

def LibrarySearch_Al(source, mode, user):
    # s3 = boto3.resource('s3', region_name="ap-southeast-2", aws_access_key_id='', 
    #                     aws_secret_access_key='')
    # dir_n = user + '/unprocessed/test/User Spectra/' + fn
    # output_ulsa = join(current_app.root_path, 
    #                      'static/tamplate', 'ULSA')
    # s3.meta.client.download_file('deco3801', '/unprocessed/test/User Spectra/bdce1266ab2d94a9.txt', output_ulsa + '/test.txt')

    # this ’data_path ’ will depend on where you save data
    data_path = join(current_app.root_path,
                        'static/data/', user,
                        'unprocessed/test/User Spectra')

    path_MB = join(current_app.root_path, 
                    'static/Pre-required_data', 
                    'MassBank_matlab.mat')

    source = source #'ESI'
    mode = mode #'POSITIVE'

    path_adducts = join(current_app.root_path, 
                         'static/Pre-required_data/adducts', 
                         'Pos_adducts.xlsx')

    path_to_spec = data_path

    output_ulsa = join(current_app.root_path, 
                        'static/tamplate', 'ULSA')

    # start up the matlab runtime engine
    l = LibrarySearch_v1.initialize()

    # this is how you run the script
    l.LibrarySearch_v1(path_MB, source, mode, path_adducts,
        path_to_spec, output_ulsa, nargout=0)

    # never forget to terminate !!!
    l.terminate ()