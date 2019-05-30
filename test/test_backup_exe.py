import subprocess
import time
import datetime as dt

def test_1():
    m = dt.datetime.now()
    tm = m.strftime("%Y%m%dT%H%M%S%Z")
    # subprocess.check_call([r"C:\Program Files (x86)\ISS\SecurOS\backup.exe", "your", "arguments", "comma", "separated"])
    subprocess.check_call([r"C:\Program Files (x86)\ISS\SecurOS\backup.exe", "--out<C:\\videoaudioConverter test\\Output>", "--cam<33>", "--from<18-03-10 18:00:00>", "--to<"+tm+">", "--archive-folder<C:\\videoaudioConverter test\\Source video>"])
