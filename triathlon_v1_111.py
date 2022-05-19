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

   def __eq__(self, other):
      return self.total_time() == other.total_time()

   def __gt__(self, other):
      return self.total_time() > other.total_time()

   def __lt__(self, other):
      return self.total_time() < other.total_time()


class Triathlon(object):

   def __init__(self):
      self.d = {}

   def add(self, t):
      self.d[t.tid] = t

   def remove(self, tid):
      if tid in self.d:
         del self.d[tid]

   def lookup(self, tid):
      if tid in self.d:
         return self.d[tid]
      else:
         return None
