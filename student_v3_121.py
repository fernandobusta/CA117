#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, cao):
        self.name = name
        self.cao = cao
        self.marks = {}

    def add_grade(self, mod, grade):
        self.marks[mod] = grade

    def get_grade(self, mod):
        if mod in self.marks:
            return self.marks[mod]
        return 'N/A'

    def total_points(self):
        glist = []
        for k, v in self.marks.items():
            glist.append(to_points(v))
        if len(glist) <= 3:
            return sum(glist)
        return sum(sorted(glist)[-3:])

    def __str__(self):
        slist = []
        slist.append('Name: {}'.format(self.name))
        slist.append('CAO: {}'.format(self.cao))
        slist.append('Points: {}'.format(self.total_points()))
        return '\n'.join(slist)

def to_points(grade):

    table = {'H1': 100, 'H2': 88, 'H3': 77, 'H4': 66, 'H5': 56, 'H6': 46, 'H7': 57, 'H8': 0, 'O1': 56, 'O2': 46, 'O3': 37, 'O4': 28, 'O5': 20, 'O6': 12, 'O7': 0, 'O8': 0}
    return table[grade]
