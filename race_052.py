#!/usr/bin/env python3

import sys

name_runs = {}
def personal(runs):
    name = runs[0]
    runs.pop(0)
    minute = []
    sec = []
    try:
        for i in runs:
            try:
                minute.append(int(i[:2]))
            except ValueError:
                minute.append(int(i[0]))
        for i in runs:
            try:
                if int(i[:2]) == min(minute):
                    sec.append(i)
            except ValueError:
                if int(i[0]) == min(minute):
                    sec.append(i)
        if len(sec) == 1:
            return name, sec
        else:
            second = []
            for i in sec:
                second.append(int(i[-2:]))
            for i in sec:
                if int(i[-2:]) == min(second):
                    return name, i
    except ValueError:
        pass


def best(runners):
    time = []
    sec = []
    for i in runners.values():
        try:
            time.append(int(i[:2]))
        except ValueError:
            time.append(int(i[0]))
    for i in runners.values():
        try:
            if int(i[:2]) == min(time):
                sec.append(i)
        except ValueError:
            if int(i[0]) == min(time):
                sec.append(i)
    best = [int(i[-2:]) for i in sec]
    best_sec = min(best)
    best_min = min(time)
    final_time = (f'{best_min}:{best_sec}')
    return final_time


runners = {}
for line in sys.stdin:
    runs = line.strip().split()
    name, time = personal(runs)
    if len(time) > 1:
        runners[name] = time
    else:
        runners[name] = time[0]
s = [i for i in runners.keys() if runners[i] == (best(runners))]
print(f'{s[0]} : {best(runners)}')
