import secrets
import os
import boto3
import LibrarySearch_v1
from os.path import join
from flask import url_for, current_app, request

def save_datafile(form_datafile, user):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_datafile.data.filename)
    fn = random_hex + f_ext
    s3 = boto3.client('s3', aws_access_key_id='AKIAJNCIGVIXH7R4MQVA', 
                        aws_secret_access_key='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')
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

def DeconvLibrarySearch_Al():
    random_hex = secrets.token_hex(8)

def ImportDeconv_Al():
    random_hex = secrets.token_hex(8)

def LibrarySearch_Al(source, mode):
    s3 = boto3.client('s3', region_name="ap-southeast-2", aws_access_key_id='AKIAJNCIGVIXH7R4MQVA', 
                        aws_secret_access_key='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')
    #dir_n = user + '/unprocessed/test/User Spectra/' + fn
    output_ulsa = join(current_app.root_path, 
                         'static/tamplate', 'ULSA')
    s3.download_file('deco3801', '/unprocessed/test/User Spectra/bdce1266ab2d94a9.txt', output_ulsa + '/test.txt')
    # # this ’data_path ’ will depend on where you save data
    # data_path = join('~ ', 'data', 'qaehs', 'sim', 'data')

    # path_MB = join(current_app.root_path, 
    #                 'static/MassBank_matlab', 
    #                 'MassBank_matlab.mat')

    # source = source #'ESI'
    # mode = mode #'POSITIVE'

    # path_adducts = join(current_app.root_path, 
    #                      'static/Pre-required_data/adducts', 
    #                      'Pos_adducts.xlsx')

    # path_to_spec = join(data_path, 'deconv')

    # output_ulsa = join(current_app.root_path, 
    #                     'static/tamplate', 'ULSA')

    # # start up the matlab runtime engine
    # l = LibrarySearch_v1.initialize()

    # # this is how you run the script
    # l.LibrarySearch_v1(path_MB, source, mode, path_adducts,
    #     path_to_spec, output_ulsa, nargout=0)

    # # never forget to terminate !!!
    # l.terminate ()