import time
import datetime as dt
from pywinauto.application import Application
from model.input_data import *
import hashlib
# import subprocess

def test_30_H264():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "30"
    out_file_name = "30_H264.avi"
    app = Application(backend="uia").start(r'"'+path_to_backupexe+'" --out "'+output_folder+out_file_name+'" --cam "' + cam_id + '" --from "'+begin_time+'" --to "' + end_time + '" --archive-path "'+path_to_archive+'"').connect(title='Утилита экспорта медиа данных')
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())

def test_31_H263():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "31"
    out_file_name = "31_H263.avi"
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '"').connect(title='Утилита экспорта медиа данных')
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())

def test_32_MPEG4():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "32"
    out_file_name = "32_MPEG4.avi"
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '"').connect(title='Утилита экспорта медиа данных')
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())

def test_33_MJPEG():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "33"
    out_file_name = "33_MJPEG.avi"
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '"').connect(title='Утилита экспорта медиа данных')
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())

def test_34_YUAN():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "34"
    out_file_name = "34_YUAN.avi"
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '"').connect(title='Утилита экспорта медиа данных')
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())

def test_35_MIX():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    cam_id = "35"
    out_file_name = "35_MIX.avi"
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '"').connect(title='Утилита экспорта медиа данных')
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())


    # subprocess.check_call(["C:\\Program Files (x86)\\ISS\\SecurOS\\backup.exe", "--out=C:\\videoaudioConverter_test\\Output\\out.avi", "--cam=33", "--from=18-03-10 18:00:00", "--to="+tm+"", "--archive-path=C:\\videoaudioConverter_test\\Source_video"]) вызов через другую библиотеку
    #dlg.child_window(auto_id="2").wait('visible',  timeout=50, retry_interval=0.5)  еще один вариант ожидания, на всякий случай

