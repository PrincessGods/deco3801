import secrets
import os
import boto3
import LibrarySearch_v1
import ImportDeconv_v1
import DeconvLibrarySearch_v1
from os.path import join
from flask import url_for, current_app, request
import subprocess

def save_datafile_L(form_datafile, user, JobID, source, mode):
    f_name, f_ext = os.path.splitext(form_datafile.data.filename)
    fn = f_name + f_ext
    output_fn = f_name + ".csv"

    MetaDataToS3(form_datafile, user, fn, JobID)
    DownloadFromS3(user, form_datafile, JobID)
    
    command = 'mkdir -p /home/ubuntu/deco3801/application/static/data/template1/' + user + '/' + JobID + '/ULSA_tmp'
    subprocess.call(command, shell=True)

    command = 'mkdir -p /home/ubuntu/deco3801/application/static/data/template2/' + user + '/' + JobID + '/ULSA'
    subprocess.call(command, shell=True)

    LibrarySearch_Al(source, mode, user, JobID)

    command = 'mv /home/ubuntu/deco3801/application/static/data/template1/' + user + '/' + JobID + '/ULSA_tmp/*.csv /home/ubuntu/deco3801/application/static/data/template2/' + user + '/' + JobID + '/ULSA/ULSA.csv'
    subprocess.call(command, shell=True)
    
    ProcessedDataToS3(user, JobID)
    RemoveFromEBS(user)
    
    return fn

def save_datafile_D(fileList, user, JobID, d_set):
    for form_datafile in fileList:
        f_name, f_ext = os.path.splitext(form_datafile.data.filename)
        fn = f_name + f_ext

        MetaDataToS3(form_datafile, user, fn, JobID)
        DownloadFromS3(user, form_datafile, JobID)
    
    command = 'mkdir -p /home/ubuntu/deco3801/application/static/data/template/' + user + '/' + JobID + '/deconv'
    subprocess.call(command, shell=True)

    ImportDeconv_Al(d_set, user, JobID)
    
    ProcessedDataToS3(user, JobID)
    RemoveFromEBS(user)
    
    return fn

def save_datafile_DL(fileList, user, JobID, d_set, source, mode):
    for form_datafile in fileList:
        f_name, f_ext = os.path.splitext(form_datafile.data.filename)
        fn = f_name + f_ext

        MetaDataToS3(form_datafile, user, fn, JobID)
        DownloadFromS3(user, form_datafile, JobID)
    
    command = 'mkdir -p /home/ubuntu/deco3801/application/static/data/template/' + user + '/' + JobID + '/ULSA'
    subprocess.call(command, shell=True)

    command = 'mkdir -p /home/ubuntu/deco3801/application/static/data/template/' + user + '/' + JobID + '/deconv'
    subprocess.call(command, shell=True)

    DeconvLibrarySearch_Al(source, mode, d_set, user, JobID)
    
    ProcessedDataToS3(user, JobID)
    RemoveFromEBS(user)
    
    return fn

def DeconvLibrarySearch_Al(source, mode, d_set, user, JobID):
    # elements in ’d_set ’ list corresponds to different chemical parameter

    # path to target list ( what we ’re looking for)
    target_path = '/home/ubuntu/deco3801/application/static/data/unprocessed/' + user + '/' + JobID + '/Target'
    
    path_low = '/home/ubuntu/deco3801/application/static/data/unprocessed/' + user + '/' + JobID + '/Low_Energy'
    path_high = '/home/ubuntu/deco3801/application/static/data/unprocessed/' + user + '/' + JobID + '/High_Energy'
    
    path_MB = join(current_app.root_path, 
                    'static/data/Pre-required_data', 
                    'MassBank_matlab.mat')

    path_adducts = join(current_app.root_path, 
                         'static/data/Pre-required_data/adducts', 
                         'Pos_adducts.xlsx')
    
    output_ulsa = join(current_app.root_path, 
                        'static/data/template', user,
                        JobID, 'ULSA')

    output_deconv = join(current_app.root_path, 
                        'static/data/template', user,
                        JobID, 'deconv')
    
    # start up the matlab runtime engine
    dl = DeconvLibrarySearch_v1 . initialize ()
    
    dl. DeconvLibrarySearch_v1 (d_set, target_path, path_low, path_high,
        path_MB, source, mode, path_adducts, output_ulsa,
        output_deconv, nargout=0)
    
    # never forget to terminate !
    dl. terminate ()
    
def ImportDeconv_Al(d_set, user, JobID):
    # elements in ’d_set ’ list corresponds to different chemical parameter
   
    # path to target list ( what we ’re looking for)
    target_path = '/home/ubuntu/deco3801/application/static/data/unprocessed/' + user + '/' + JobID + '/Target'
    
    path_low = '/home/ubuntu/deco3801/application/static/data/unprocessed/' + user + '/' + JobID + '/Low_Energy'
    path_high = '/home/ubuntu/deco3801/application/static/data/unprocessed/' + user + '/' + JobID + '/High_Energy'
    output_deconv = join(current_app.root_path, 
                        'static/data/template', user,
                        JobID, 'deconv')
    
    # start up the matlab runtime engine
    d = ImportDeconv_v1.initialize()
    
    # this is how you run the script
    d.ImportDeconv_v1 (d_set, target_path, path_low, path_high, nargout =0)
    
    # dont forget to terminate the runtime engine at end of run!
    d.terminate ()

def LibrarySearch_Al(source, mode, user, JobID):
    path_MB = join(current_app.root_path, 
                    'static/data/Pre-required_data', 
                    'MassBank_matlab.mat')

    path_adducts = join(current_app.root_path, 
                         'static/data/Pre-required_data/adducts', 
                         'Pos_adducts.xlsx')

    path_to_spec = '/home/ubuntu/deco3801/application/static/data/unprocessed/' + user + '/' + JobID + '/User_Spectra'

    output_ulsa = join(current_app.root_path, 
                        'static/data/template1', user,
                        JobID, 'ULSA_tmp')

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
    command = 'sudo aws s3 cp --recursive application/static/data/template2/' + user + '/' + JobID + ' s3://deco3801mars/' + user + '/' + JobID + '/processed'

    subprocess.call(command, shell=True)

def RemoveFromEBS(user):
    command = 'sudo rm -R /home/ubuntu/deco3801/application/static/data/template1/' + user
    subprocess.call(command, shell=True)

    command = 'sudo rm -R /home/ubuntu/deco3801/application/static/data/template2/' + user
    subprocess.call(command, shell=True)

    command = 'sudo rm -R /home/ubuntu/deco3801/application/static/data/unprocessed/' + user
    subprocess.call(command, shell=True)

def DownloadFromS3ToLocal(user, JobID):
    command = 'mkdir -p /home/ubuntu/deco3801/application/static/data/download/' + user + '/' + JobID 
    subprocess.call(command, shell=True)

    s3 = boto3.client('s3')
    key = user + '/' + JobID + '/processed/ULSA/ULSA.csv'
    url = join('http://', request.host, 
                'static/data/download', user, JobID)
    filename = 'application/static/data/download/' + user + '/' + JobID + '/download.csv'
    s3.download_file(Bucket='deco3801mars', Key=key, Filename=filename)
    return url
    #s3.meta.client.download_file('deco3801mars', key, 'application/download.csv')