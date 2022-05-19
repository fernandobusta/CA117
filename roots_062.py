#!/usr/bin/env python3

import sys
import math

def findroots(a, b, c):
    st1 = b * b - 4 * a * c
    if st1 >= 0:
        st2 = math.sqrt(st1)
        r1 = (-b + st2) / (2 * a)
        r2 = (-b - st2) / (2 * a)
        return (f'r1 = {r1}, r2 = {r2}')
    else:
        return None


for line in sys.stdin:
    nums = [int(n) for n in line.strip().split()]
    roots = findroots(nums[0], nums[1], nums[2])
    print(roots)
