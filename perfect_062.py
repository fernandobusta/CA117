#!/usr/bin/env python3

import sys

def sum_factors(s):
    factors = []
    for i in range(1, s // 2 + 1):
        if s % i == 0:
            factors.append(i)
    return sum(factors)


def is_perfect(s, sums):
    return sums == s


for line in sys.stdin:
    s = int(line.strip())
    sums = sum_factors(s)
    print(is_perfect(s, sums))
