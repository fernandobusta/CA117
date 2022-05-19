#!/usr/bin/env python3

import sys

def extract_m_three(num):
    new = ['X' if not num % 3 else num for num in range(num + 1)]
    new.pop(0)
    return new


for num in sys.stdin:
    num = int(num.strip())
    print(f'Multiples of 3 replaced: {extract_m_three(num)}')
