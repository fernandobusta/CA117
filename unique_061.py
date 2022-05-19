#!/usr/bin/env python3

import sys

def largest(num):
    single = sorted(set(num))
    count = {}
    for i in single:
        count[i] = num.count(i)
    unique = []
    for i in count:
        if count[i] == 1:
            unique.append(i)
    if len(unique) > 0:
        return max(unique)
    else:
        return 'none'


for line in sys.stdin:
    num = [int(n) for n in line.strip().split()]
    print(largest(num))
