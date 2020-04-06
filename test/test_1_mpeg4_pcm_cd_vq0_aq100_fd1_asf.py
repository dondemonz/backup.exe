import time
import datetime as dt
from pywinauto.application import Application
from model.input_data import *
import hashlib
from model.hash_sums import *
import os
# import subprocess


def test_30_H264(fix):
    cam_id = "30"
    out_file_name = "30_H264.asf"
    video_codec = "MPEG4"
    audio_codec = "PCM"
    span = "cd"
    video_quality = "0"
    audio_quality = "100"
    fps_divider = "1"

    #end_time = take_timestamp()

    app = start_app_backup(audio_codec, audio_quality, cam_id, fix.end_time, fps_divider, out_file_name, span, video_codec, video_quality)
    start_process_backup(app)

    hasher = take_hash_sum(out_file_name)
    assert hasher.hexdigest() == hash1_H264
    os.remove(''+output_folder + out_file_name+'')


def take_hash_sum(out_file_name):
    hasher = hashlib.md5()
    with open('' + output_folder + out_file_name + '', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    return hasher


def start_process_backup(app):
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()


def start_app_backup(audio_codec, audio_quality, cam_id, end_time, fps_divider, out_file_name, span, video_codec, video_quality):
    app = Application(backend="uia").start(
        r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec "' + video_codec + '" --audio-codec "' + audio_codec + '" --span "' + span + '" --video-quality "' + video_quality + '" --audio-quality "' + audio_quality + '" --fps-divider "' + fps_divider + '"').connect(
        title='Утилита экспорта медиа данных')
    return app


def take_timestamp():
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    return end_time


def test_31_H263():
    cam_id = "31"
    out_file_name = "31_H263.asf"
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec MPEG4 --audio-codec PCM --span cd --video-quality 0 --audio-quality 100 --fps-divider 1').connect(title=title)
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    assert hasher.hexdigest() == hash1_H263
    os.remove(''+output_folder + out_file_name+'')

def test_32_MPEG4():
    cam_id = "32"
    out_file_name = "32_MPEG4.asf"
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec MPEG4 --audio-codec PCM --span cd --video-quality 0 --audio-quality 100 --fps-divider 1').connect(title=title)
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    assert hasher.hexdigest() == hash1_MPEG4
    os.remove(''+output_folder + out_file_name+'')

def test_33_MJPEG():
    cam_id = "33"
    out_file_name = "33_MJPEG.asf"
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec MPEG4 --audio-codec PCM --span cd --video-quality 0 --audio-quality 100 --fps-divider 1').connect(title=title)
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    assert hasher.hexdigest() == hash1_MJPEG
    os.remove(''+output_folder + out_file_name+'')

def test_34_YUAN():
    cam_id = "34"
    out_file_name = "34_YUAN.asf"
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec MPEG4 --audio-codec PCM --span cd --video-quality 0 --audio-quality 100 --fps-divider 1').connect(title=title)
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    assert hasher.hexdigest() == hash1_YUAN
    os.remove(''+output_folder + out_file_name+'')

def test_61_MxPEG():
    cam_id = "31"
    out_file_name = "61_MxPEG.asf"
    m = dt.datetime.now()
    end_time = m.strftime("%Y%m%dT%H%M%S%Z")
    app = Application(backend="uia").start(r'"' + path_to_backupexe + '" --out "' + output_folder + out_file_name + '" --cam "' + cam_id + '" --from "' + begin_time + '" --to "' + end_time + '" --archive-path "' + path_to_archive + '" --video-codec MPEG4 --audio-codec PCM --span cd --video-quality 0 --audio-quality 100 --fps-divider 1').connect(title=title)
    dlg = app.window(title='Утилита экспорта медиа данных')
    dlg1 = dlg.child_window(auto_id="2")
    dlg1.wait('visible', timeout=150)
    dlg.child_window(auto_id="2").click()

    hasher = hashlib.md5()
    with open(''+output_folder + out_file_name+'', 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    assert hasher.hexdigest() == hash1_MxPEG
    os.remove(''+output_folder + out_file_name+'')

    # subprocess.check_call(["C:\\Program Files (x86)\\ISS\\SecurOS\\backup.exe", "--out=C:\\videoaudioConverter_test\\Output\\out.avi", "--cam=33", "--from=18-03-10 18:00:00", "--to="+tm+"", "--archive-path=C:\\videoaudioConverter_test\\Source_video"]) вызов через другую библиотеку
    # dlg.child_window(auto_id="2").wait('visible',  timeout=50, retry_interval=0.5)  еще один вариант ожидания, осталю тут на всякий случай

