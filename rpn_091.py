#!/usr/bin/env python3

from math import sqrt

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


binops = {'+': float.__add__,
          '-': float.__sub__,
          '*': float.__mul__,
          '/': float.__truediv__}

uniops = {'n': float.__neg__,
          'r': sqrt}


def calculator(chars):

    s = Stack()
    for c in chars.split():
        try:
            s.push(float(c))

        except ValueError:
            if s.is_empty() is False:
                if c in binops.keys():
                    last = s.pop()
                    suma = binops[c](s.pop(), last)
                    s.push(suma)
                elif c in uniops.keys():
                    suma = uniops[c](s.pop())
                    s.push(suma)

    return s.top()
