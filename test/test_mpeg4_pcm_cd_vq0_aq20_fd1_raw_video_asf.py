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
    out_file_name = "30_H264.asf"
    app = Application(backend="uia").start(r'"'+path_to_backupexe+'" --out "'+output_folder+out_file_name+'" --cam "' + cam_id + '" --from "'+begin_time+'" --to "' + end_time + '" --archive-path "'+path_to_archive+'" --video-codec MPEG4 --audio-codec PCM --span cd --video-quality 0 --audio-quality 20 --fps-divider 1 --raw-video').connect(title='Утилита экспорта медиа данных')
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    #assert hasher.hexdigest() == hash1_H264
    os.remove(''+output_folder + out_file_name+'')

def test_31_H263():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "31"
    out_file_name = "31_H263.asf"
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec MPEG4 --audio-codec PCM --span cd --video-quality 0 --audio-quality 20 --fps-divider 1 --raw-video ').connect(title='Утилита экспорта медиа данных')
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    #assert hasher.hexdigest() == hash1_H263
    os.remove(''+output_folder + out_file_name+'')

def test_32_MPEG4():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "32"
    out_file_name = "32_MPEG4.asf"
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec MPEG4 --audio-codec PCM --span cd --video-quality 0 --audio-quality 20 --fps-divider 1 --raw-video').connect(title='Утилита экспорта медиа данных')
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    #assert hasher.hexdigest() == hash1_MPEG4
    os.remove(''+output_folder + out_file_name+'')

def test_33_MJPEG():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "33"
    out_file_name = "33_MJPEG.asf"
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec MPEG4 --audio-codec PCM --span cd --video-quality 0 --audio-quality 20 --fps-divider 1 --raw-video').connect(title='Утилита экспорта медиа данных')
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    #assert hasher.hexdigest() == hash1_MJPEG
    os.remove(''+output_folder + out_file_name+'')

def test_34_YUAN():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "34"
    out_file_name = "34_YUAN.asf"
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec MPEG4 --audio-codec PCM --span cd --video-quality 0 --audio-quality 20 --fps-divider 1 --raw-video').connect(title='Утилита экспорта медиа данных')
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    #assert hasher.hexdigest() == hash1_YUAN
    os.remove(''+output_folder + out_file_name+'')

def test_61_MxPEG():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "31"
    out_file_name = "61_MxPEG.asf"
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec MPEG4 --audio-codec PCM --span cd --video-quality 0 --audio-quality 20 --fps-divider 1 --raw-video').connect(title='Утилита экспорта медиа данных')
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    #assert hasher.hexdigest() == hash1_MxPEG
    os.remove(''+output_folder + out_file_name+'')





"""
#тест убрал, т.к. при открытии через visual builder он отключен. И при экспорте backup.exe не может не разделять файлы с разными потоками (занимается этим конвертер) 
def test_35_MIX():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "35"
    out_file_name = "35_MIX.avi"
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '"').connect(title='Утилита экспорта медиа данных')
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=170)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    #assert hasher.hexdigest() == hash_MIX
"""
    # subprocess.check_call(["C:\\Program Files (x86)\\ISS\\SecurOS\\backup.exe", "--out=C:\\videoaudioConverter_test\\Output\\out.avi", "--cam=33", "--from=18-03-10 18:00:00", "--to="+tm+"", "--archive-path=C:\\videoaudioConverter_test\\Source_video"]) вызов через другую библиотеку
    #dlg.child_window(auto_id="2").wait('visible',  timeout=50, retry_interval=0.5)  еще один вариант ожидания, на всякий случай

