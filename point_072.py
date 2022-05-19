#!/usr/bin/env python3

from re import findall
import math

class Point(object):

    def __init__(p, x=0, y=0):
        p.x = x
        p.y = y

    def distance(p, other):
        p1 = str(p)
        p2 = str(other)
        getpoint = r'\d[.]\d'
        px, py = findall(getpoint, p1)
        px = float(px)
        py = float(py)
        p2x, p2y = findall(getpoint, p2)
        p2x = float(p2x)
        p2y = float(p2y)
        return calc_dist(px, py, p2x, p2y)

    def __str__(p):
        return '({:.1f}, {:.1f})'.format(p.x, p.y)

def calc_dist(px, py, p2x, p2y):
    sum = (px - p2x) ** 2 + (py - p2y) ** 2
    dist = math.sqrt(sum)
    return dist
