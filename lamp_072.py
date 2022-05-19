#!/usr/bin/env python3

class Lamp(object):

    def __init__(lamp, on=False):
        lamp.on = on

    def turn_on(lamp):
        lamp.on = True

    def turn_off(lamp):
        lamp.on = False

    def toggle(lamp):
        if lamp.on is False:
            lamp.on = True
        else:
            lamp.on = False
