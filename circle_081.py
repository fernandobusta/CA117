#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, other):
        x = (other.x + self.x) / 2
        y = (other.y + self.y) / 2
        return Point(x, y)

    def __str__(self):
        return '({:.1f}, {:.1f})'.format(self.x, self.y)


class Circle(object):

    def __init__(self, centre=None, radius=1):
        if centre is None:
            centre = Point()
        self.centre = centre
        self.radius = radius

    def __str__(self):
        lines = []
        lines.append('Centre: {}'.format(self.centre))
        lines.append('Radius: {}'.format(self.radius))
        return '\n'.join(lines)
