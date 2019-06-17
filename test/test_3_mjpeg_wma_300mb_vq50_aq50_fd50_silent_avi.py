import time
import datetime as dt
from pywinauto.application import Application
from model.input_data import *
import hashlib
from model.hash_sums import *
import os
# import subprocess


def test_30_H264():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "30"
    out_file_name = "30_H264.avi"
    Application(backend="uia").start(r'"'+path_to_backupexe+'" --out "'+output_folder+out_file_name+'" --cam "' + cam_id + '" --from "'+begin_time+'" --to "' + end_time + '" --archive-path "'+path_to_archive+'" --video-codec MJPEG --audio-codec WMA --span 300 --video-quality 50 --audio-quality 50 --fps-divider 50 --silent')
    time.sleep(5)

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    assert hasher.hexdigest() == hash3_H264
    os.remove(''+output_folder + out_file_name+'')

def test_31_H263():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "31"
    out_file_name = "31_H263.avi"
    Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec MJPEG --audio-codec WMA --span 300 --video-quality 50 --audio-quality 50 --fps-divider 50 --silent')
    time.sleep(5)

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    assert hasher.hexdigest() == hash3_H263
    os.remove(''+output_folder + out_file_name+'')

def test_32_MPEG4():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "32"
    out_file_name = "32_MPEG4.avi"
    Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec MJPEG --audio-codec WMA --span 300 --video-quality 50 --audio-quality 50 --fps-divider 50 --silent')
    time.sleep(5)

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    assert hasher.hexdigest() == hash3_MPEG4
    os.remove(''+output_folder + out_file_name+'')

def test_33_MJPEG():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "33"
    out_file_name = "33_MJPEG.avi"
    Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec MJPEG --audio-codec WMA --span 300 --video-quality 50 --audio-quality 50 --fps-divider 50 --silent')
    time.sleep(15)

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    assert hasher.hexdigest() == hash3_MJPEG
    os.remove(''+output_folder + out_file_name+'')

def test_34_YUAN():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "34"
    out_file_name = "34_YUAN.avi"
    Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec MJPEG --audio-codec WMA --span 300 --video-quality 50 --audio-quality 50 --fps-divider 50 --silent')
    time.sleep(10)

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    assert hasher.hexdigest() == hash3_YUAN
    os.remove(''+output_folder + out_file_name+'')

def test_61_MxPEG():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "31"
    out_file_name = "61_MxPEG.avi"
    Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec MJPEG --audio-codec WMA --span 300 --video-quality 50 --audio-quality 50 --fps-divider 50 --silent')
    time.sleep(5)

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    assert hasher.hexdigest() == hash3_MxPEG
    os.remove(''+output_folder + out_file_name+'')

