#!/usr/bin/env python3

import sys

def poker(cards):
    strength = {}
    for s in cards:
        if s in strength:
            strength[s] += 1
        else:
            strength[s] = 1
    #get max value of dict
    maxvalue = max(strength.values())
    return maxvalue


for line in sys.stdin:
    tokens = line.strip().split()
    cards = [i[0] for i in tokens]
    print(poker(cards))
