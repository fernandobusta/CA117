#!/usr/bin/env python3

class Score(object):

    #set the variables in the class
    def __init__(s, goals=0, points=0):
        s.goals = goals
        s.points = points

    #turn the score into points
    def total_score(s):
        return s.points + (s.goals * 3)

    #add two instances
    def __add__(s, other):
        tg = s.goals + other.goals
        tp = s.points + other.points
        #we have to create another score
        return Score(tg, tp)

    #update instance -> inplace addition(+=)
    def __iadd__(s, other):
        s.goals += other.goals
        s.points += other.points
        return s

    #less than
    def __lt__(s, other):
        return s.total_score() < other.total_score()

    #less than or equal to
    def __le__(s, other):
        return s.total_score() <= other.total_score()

    #greater than or equal to
    def __ge__(s, other):
        return s.total_score() >= other.total_score()

    #is greater than
    def __gt__(s, other):
        return s.total_score() > other.total_score()

    def __ne__(s, other):
        return s.total_score() != other.total_score()

    #equal method(==)
    def __eq__(s, other):
        return s.total_score() == other.total_score()

    #print results
    def __str__(s):
        return '{} goal(s) and {} point(s)'.format(s.goals, s.points)
