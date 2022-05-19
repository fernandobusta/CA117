#!/usr/bin/env python3

import sys

def dec(num):
    from math import pi
    return (f'{pi:.{num}f}')


for num in sys.stdin:
    num = int(num.strip())
    print(dec(num))
