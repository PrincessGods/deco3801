import secrets
import os
import boto3
import LibrarySearch_v1
from os.path import join
from flask import url_for, current_app, request
import subprocess

def run_before(lastfunc, *args1, **kwargs1):
    def run(func):
        def wrapped_func(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except:
                result = None
            finally:
                lastfunc(*args1, **kwargs1)
                return result
        return wrapped_func
    return run

def save_datafile(fileList, user, JobID, method):
    for form_datafile in fileList:
        f_name, f_ext = os.path.splitext(form_datafile.data.filename)
        fn = f_name + f_ext

        MetaDataToS3(form_datafile, user, fn, JobID)
        DownloadFromS3(user, form_datafile, JobID)
    
    if chosenMethod == 'ImportDeconv':
        ImportDeconv_Al() 
    elif chosenMethod == 'LibrarySearch':
        command = 'sudo mkdir application/static/data/template/' + user + '/' + JobID + '/ULSA'
        subprocess.call(command, shell=True)
        
        LibrarySearch_Al('ESI', 'POSITIVE', user, JobID)
    else:
        DeconvLibrarySearch_Al()
    
    ProcessedDataToS3(user, JobID)
    
    return fn

def DeconvLibrarySearch_Al():
    random_hex = secrets.token_hex(8)

def ImportDeconv_Al():
    random_hex = secrets.token_hex(8)

def LibrarySearch_Al(source, mode, user, JobID):
    data_path = join(current_app.root_path,
                        'static/data/unprocessed', user,
                        JobID, 'User_Spectra')

    path_MB = join(current_app.root_path, 
                    'static/data/Pre-required_data', 
                    'MassBank_matlab.mat')

    source = source #'ESI'
    mode = mode #'POSITIVE'

    path_adducts = join(current_app.root_path, 
                         'static/data/Pre-required_data/adducts', 
                         'Pos_adducts.xlsx')

    path_to_spec = '/home/ubuntu/deco3801/application/static/data/unprocessed/' + user + '/' + JobID + '/User_Spectra'

    output_ulsa = join(current_app.root_path, 
                        'static/data/template', user,
                        JobID, 'ULSA')

    # start up the matlab runtime engine
    l = LibrarySearch_v1.initialize()

    # this is how you run the script
    l.LibrarySearch_v1(path_MB, source, mode, path_adducts,
        path_to_spec, output_ulsa, nargout=0)

    # never forget to terminate !!!
    l.terminate ()

def MetaDataToS3(file, user, fn, JobID):
    s3 = boto3.client('s3')
    bucket_name = 'deco3801mars'

    if file.id == 'xlsxFile':
        dir_n = user + '/' + JobID + '/unprocessed/Target/' + fn
    elif file.id == 'VANFileLow':
        dir_n = user + '/' + JobID + '/unprocessed/Low_Energy/' + fn
    elif file.id == 'VANFileHigh':
        dir_n = user + '/' + JobID + '/unprocessed/High_Energy/' + fn
    else:
        dir_n = user + '/' + JobID + '/unprocessed/User_Spectra/' + fn

    s3.put_object(Bucket=bucket_name, Key=dir_n, Body=file.data)

def DownloadFromS3(user, file, JobID):
    if file.id == 'xlsxFile':
        command = 'sudo aws s3 sync s3://deco3801mars/' + user + '/' + JobID + '/unprocessed/Target application/static/data/unprocessed/' + user + '/' + JobID + '/Target'
    elif file.id == 'VANFileLow':
        command = 'sudo aws s3 sync s3://deco3801mars/' + user + '/' + JobID + '/unprocessed/Low_Energy application/static/data/unprocessed/' + user +  '/' + JobID + '/Low_Energy'
    elif file.id == 'VANFileHigh':
        command = 'sudo aws s3 sync s3://deco3801mars/' + user + '/' + JobID + '/unprocessed/High_Energy application/static/data/unprocessed/' + user +  '/' + JobID + '/High_Energy'
    else:
        command = 'sudo aws s3 sync s3://deco3801mars/' + user + '/' + JobID + '/unprocessed/User_Spectra application/static/data/unprocessed/' + user +  '/' + JobID + '/User_Spectra'

    subprocess.call(command, shell=True)

def ProcessedDataToS3(user, JobID):
    command = 'sudo aws s3 cp --recursive application/static/data/unprocessed/' + user + '/' + JobID + 's3://deco3801mars/' + user + '/' + JobID + '/processed'

    subprocess.call(command, shell=True)

#def RemoveFromEBS(user):