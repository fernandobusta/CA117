#!/usr/bin/env python3

class Stack(object):

    def __init__(self):
        self.slist = []

    def push(self, e):
        self.slist.append(e)

    def pop(self):
        if len(self) > 0:
            return self.slist.pop()

    def top(self):
        return self.slist[-1]

    def is_empty(self):
        return len(self.slist) == 0

    def __len__(self):
        return len(self.slist)


d = {')': '(', '}': '{', ']': '['}
def matcher(line):

    s = Stack()

    for c in line:

        if c in d.values():
            s.push(c)

        elif c in d.keys():
            if d[c] != s.pop():
                return False

    return s.is_empty()
