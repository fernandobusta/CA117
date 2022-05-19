#!/usr/bin/env python3

class Triathlete(object):

   def __init__(self, name, tid):
      self.name = name
      self.tid = tid
      self.races = {}

   def __str__(self):
      return 'Name: {}\nID: {}\nRace time: {}'.format(self.name, self.tid, self.total_time())

   def add_time(self, discipline, time):
      self.races[discipline] = time

   def get_time(self, discipline):
      return self.races[discipline]

   def total_time(self):
        return sum(self.races.values())
