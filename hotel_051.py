#!/usr/bin/env python3

import sys

def available(rooms, booked):
    sorted(booked)
    for i in range(1, rooms):
        if i not in booked:
            free = i
            return free
    return 'no room'


for line in sys.stdin:
    booked = [int(n) for n in line.strip().split()]
    rooms = booked[0]
    booked.pop(0)
    print(available(rooms, booked))
