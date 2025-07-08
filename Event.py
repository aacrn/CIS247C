#Aaron Truong
#Event Hw4 CIS 247 C

from Date import Date

class Event:
    def __init__(self, event_name, start_hour, end_hour, event_date):
        self.event_name = event_name
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.event_date = event_date

    @property
    def event_name(self):
        return self._event_name

    @event_name.setter
    def event_name(self, value):
        self._event_name = value

    @property
    def start_hour(self):
        return self._start_hour

    @start_hour.setter
    def start_hour(self, value):
        self._start_hour = value

    @property
    def end_hour(self):
        return self._end_hour

    @end_hour.setter
    def end_hour(self, value):
        self._end_hour = value

    @property
    def event_date(self):
        return self._event_date

    @event_date.setter
    def event_date(self, value):
        self._event_date = value

    def __str__(self):
        return f"Event: {self.event_name}, Time: {self.start_hour} to {self.end_hour}, Date: {self.event_date}"

    def overlaps_with(self, other):
        if self.event_date != other.event_date:
            return False
        return self.start_hour < other.end_hour and other.start_hour < self.end_hour