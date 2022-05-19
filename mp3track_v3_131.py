#!/usr/bin/env python3

class MP3Track(object):

   def __init__(self, title, duration, artist=[]):
      self.title = title
      self.duration = duration
      self.artist = artist

   def add_artist(self, new_art):
      self.artist.append(new_art)

   def __str__(self):
      slist = []
      slist.append('Title: {}'.format(self.title))
      slist.append('By: {}'.format(', '.join(self.artist)))
      slist.append('Duration: {}'.format(self.duration))
      return '\n'.join(slist)
