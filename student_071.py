#!/usr/bin/env python3

class Student(object):

    def set_attributes(s, sid, name, modlist):
        s.sid = sid
        s.name = name
        s.modlist = modlist

    def print_attributes(s):
        print(f'ID: {s.sid}\nName: {s.name}\nModules: {", ".join(s.modlist)}')

    def add_module(s, am):
        s.modlist.append(am)
        set(s.modlist)

    def del_module(s, dm):
        s.modlist.remove(dm)
