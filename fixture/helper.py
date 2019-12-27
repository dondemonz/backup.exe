import datetime as dt

class Helper:
    def __init__(self, end_time=""):
        self.end_time = end_time

    def take_timestamp(self):
        m = dt.datetime.now()
        end_time = m.strftime("%Y%m%dT%H%M%S%Z")
        return end_time
