#!/usr/bin/env python3

import calendar
import sys


poem = {0: "Monday's child is fair of face.",
        1: "Tuesday's child is full of grace.",
        2: "Wednesday's child is full of woe.",
        3: "Thursday's child has far to go.",
        4: "Friday's child is loving and giving.",
        5: "Saturday's child works hard for a living.",
        6: "'Sunday's child is fair and wise and good in every way."}


days = {0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'}

for date in sys.stdin:
    date = date.strip()
    [day, month, year] = date.split()
    day_of_week = calendar.weekday(int(year), int(month), int(day))
    #if statement in case it isn't a weekday
    if day_of_week in days:
        print('You were born on a ' + days[day_of_week] + ' and ' + poem[day_of_week])
