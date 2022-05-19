#!/usr/bin/env python3

class MP3Track(object):

   def __init__(self, title, duration):
      self.title = title
      self.duration = duration

   def __str__(self):
      slist = []
      slist.append('Title: {}'.format(self.title))
      slist.append('Duration: {}'.format(self.duration))
      return '\n'.join(slist)


class MP3Collection(object):

   def __init__(self):
      self.t = {}

   def add(self, other):
      self.t[other.title] = other

   def remove(self, other):
      if other in self.t:
         del self.t[other]

   def lookup(self, other):
      if other in self.t:
         return self.t[other]
      return None
