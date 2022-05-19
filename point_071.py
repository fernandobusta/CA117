#!/usr/bin/env python3

class Point(object):

    def set_attributes(p, x, y):
        p.x = x
        p.y = y

    def print_attributes(p):
        print('x: {:.2f}\ny: {:.2f}'.format(p.x, p.y))

    def reflect(p):
        p.x = -(p.x)
        p.y = -(p.y)
