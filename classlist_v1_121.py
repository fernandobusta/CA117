#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, cao):
        self.name = name
        self.cao = cao

    def __str__(self):
        slist = []
        slist.append('Name: {}'.format(self.name))
        slist.append('CAO: {}'.format(self.cao))
        return '\n'.join(slist)

class Classlist(object):

    def __init__(self):
        self.d = {}

    def add(self, s):
        self.d[s.cao] = s

    def remove(self, cao):
        if cao in self.d:
            del(self.d[cao])

    def lookup(self, cao):
        if cao in self.d:
            return self.d[cao]
        return None
