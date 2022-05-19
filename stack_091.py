#!/usr/bin/env python3

class Stack(object):

    def __init__(self):
        self.slist = []

    def push(self, e):
        self.slist.append(e)

    def pop(self):
        return self.slist.pop()

    def top(self):
        return self.slist[-1]

    def is_empty(self):
        return len(self.slist) == 0

    def __len__(self):
        return len(self.slist)
