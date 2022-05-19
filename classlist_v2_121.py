#!/usr/bin/env python3

def sort_on(s):
    return s.cao

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

    def __str__(self):
        slist = [f'{s}' for s in sorted(self.d.values(), key=sort_on)]
        return '\n'.join(slist)
