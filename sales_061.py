#!/usr/bin/env python3

import sys

def average(sales):
    return (f'{(sum(sales) / len(sales)):.2f}')


avg = []
team = {}
for line in sys.stdin:
    tokens = line.strip().split(':')
    name = tokens[0]
    sales = [int(n) for n in tokens[1].strip().split(',')]
    team[average(sales)] = name
    avg.append(float(average(sales)))

avg = sorted(avg)[::-1]
for i in avg:
    i = (f'{i:.2f}')
    print(f'{team[i]}: {i}')
