#!/usr/bin/env python3

class Score(object):

    def __init__(s, goals=0, points=0):
        s.goals = goals
        s.points = points

    def __str__(s):
        return '{} goal(s) and {} point(s)'.format(s.goals, s.points)
