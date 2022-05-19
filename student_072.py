#!/usr/bin/env python3

class Student(object):

    def __init__(s, sid, name, modlist=None):
        if modlist is None:
            modlist = []
        s.sid = sid
        s.name = name
        s.modlist = modlist

    def add_module(s, mod):
        if mod not in s.modlist:
            s.modlist.append(mod)

    def del_module(s, mod):
        if mod in s.modlist:
            s.modlist.remove(mod)

    def __str__(s):
        return 'ID: {}\nName: {}\nModules: {}'.format(s.sid, s.name, ', '.join(s.modlist))
