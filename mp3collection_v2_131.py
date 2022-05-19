#!/usr/bin/env python3

def get_artist(track):
   return track.title

class MP3Track(object):

   def __init__(self, title, duration, artist):
      self.title = title
      self.duration = duration
      self.artist = artist

   def __str__(self):
      slist = []
      slist.append('Title: {}'.format(self.title))
      slist.append('By: {}'.format(', '.join(self.artist)))
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

   def get_mp3s_by_artist(self, a):
      alist = []
      for track in self.t.values():
         if a in track.artist:
            alist.append(track)
      return alist
