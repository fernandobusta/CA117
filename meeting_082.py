#!/usr/bin/env python3

class Meeting(object):

    def __init__(self, hour, minute, duration):
         self.hour = hour
         self.minute = minute
         self. duration = duration

    def __str__(self):
        if len(str(self.hour)) == 1:
            self.hour = '0' + str(self.hour)
        if len(str(self.minute)) == 1:
            self.minute = '0' + str(self.minute)
        return '{}:{} ({} minutes)'.format(self.hour, self.minute, self.duration)
