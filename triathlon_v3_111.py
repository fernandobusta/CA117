#!/usr/bin/env python3

def sort_on(t):
   return t.name

def max_race(t):
   return t.total_time()

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
         del(self.d[tid])

   def lookup(self, tid):
      if tid in self.d:
         return self.d[tid]
      else:
         return None

   def best(self):
      lines = [f'{t}' for t in sorted(self.d.values(), key=max_race)]
      return lines[0]

   def worst(self):
      lines = [f'{t}' for t in sorted(self.d.values(), key=max_race)]
      return lines[-1]

   def __str__(self):
      slist = [f'{t}' for t in sorted(self.d.values(), key=sort_on)]
      return '\n'.join(slist)
