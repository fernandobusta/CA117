#!/usr/bin/env python3

import sys

def sortplayers(players):
    scores = sorted([n for n in players.keys()])
    return scores


players = {}
disc = []
for line in sys.stdin:
    tokens = line.strip().split()
    name = ' '.join(tokens[:-3])
    try:
        holes = [int(n) for n in tokens[-3:]]
        total = sum(holes)
        players[total] = name
    except ValueError:
        disc.append(name)

for i in sortplayers(players):
    print(f'{players[i]}: {i}')

if len(disc) > 0:
    print(f'Disqualified: {", ".join(disc)}')
