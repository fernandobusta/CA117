#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, cao):
        self.name = name
        self.cao = cao

    def __str__(self):
        return 'Name: {}\nCAO: {}'.format(self.name, self.cao)
