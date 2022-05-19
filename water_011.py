#!/usr/bin/env python3

import sys

def capacity(litres, buckets):
    i = 0
    current = int(buckets[i])
    while (litres - current >= 0) and i < len(buckets) - 1:
        litres = litres - current
        i += 1
        current = int(buckets[i])
        if (i == len(buckets) - 1) and (litres - int(buckets[i]) >= 0):
            i += 1
    return i


lines = []

for s in sys.stdin:
    s.strip()
    lines.append(s)

litres = int(lines[0].strip())
buckets = lines[1].strip().split(' ')
print(capacity(litres, buckets))
