#!/usr/bin/env python3

def sort_on(s):
    return s.cao

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

    def most_popular_subject(self):
        all = [m.marks for m in self.d.values()]
        mods = []
        for s in all:
            for m in s.keys():
                mods.append(m)
        counter = {}
        for m in mods:
            if m not in counter:
                counter[m] = 1
            else:
                counter[m] += 1
        return max(counter, key=counter.get)

    def __str__(self):
        slist = [f'{s}' for s in sorted(self.d.values(), key=sort_on)]
        return '\n'.join(slist)
