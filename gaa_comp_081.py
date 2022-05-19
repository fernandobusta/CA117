#!/usr/bin/env python3

class Score(object):

    def __init__(s, goals=0, points=0):
        s.goals = goals
        s.points = points

    def total_score(s):
        return s.goals + (s.points * 3)

    def __lt__(s, other):
        return s.total_score() < other.total_score()

    def __le__(s, other):
        return s.total_score() <= other.total_score()

    def __gt__(s, other):
        return s.total_score() > other.total_score()

    def __ne__(s, other):
        return s.total_score() != other.total_score()

    def __eq__(s, other):
        return s.goals, s.points == other.goals, other.points

    def __str__(s):
        return '{} goal(s) and {} point(s)'.format(s.goals, s.points)
