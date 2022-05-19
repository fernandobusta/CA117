#!/usr/bin/env python3

class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return '{} {} {}'.format(self.name, self.phone, self.email)

class ContactList(object):

    def __init__(self):
        self.d = {}

    def add(self, c):
        #mapping from contact name to contact details
        self.d[c.name] = c

    def remove(self, name):
        if name in self.d:
            del self.d[name]

    def get(self, name):
        if name in self.d:
            return self.d[name]
        else:
            return None

    def __str__(self):
        lines = []
        lines.append('Contact list')
        lines.append('------------')
        for n, c in sorted(self.d.items()):
            lines.append('{}'.format(c))
        return '\n'.join(lines)
