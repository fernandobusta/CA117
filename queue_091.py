#!/usr/bin/env python3

class Queue(object):

    def __init__(self):
        self.qlist = []

    def enqueue(self, e):
        self.qlist.insert(0, e)

    def dequeue(self):
        return self.qlist.pop()

    def first(self):
        return self.qlist[-1]

    def is_empty(self):
        return len(self.qlist) == 0

    def __len__(self):
        return len(self.qlist)
