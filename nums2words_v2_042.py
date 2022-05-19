#!/usr/bin/env python3

import sys

def convert(numx):
    num = {0: 'zero',
           1: 'one',
           2: 'two',
           3: 'three',
           4: 'four',
           5: 'five',
           6: 'six',
           7: 'seven',
           8: 'eight',
           9: 'nine',
           10: 'ten',
           'x': 'unknown'}
    n_replaced = ''
    for n in numx:
        n_replaced += ' ' + num[n]
    return n_replaced.strip()


for line in sys.stdin:
    numbers = line.strip().split(' ')
    numx = []
    i = 0
    while i < len(numbers):
        try:
            if len(numbers[i]) > 1 and numbers[i] != '10':
                numx.append('x')
            else:
                numx.append(int(numbers[i]))
        except ValueError:
            numx.append('x')
        i += 1
    print(convert(numx))
