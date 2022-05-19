#!/usr/bin/env python3

import sys

def repl_num(numbers):
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
           10: 'ten'}
    num_int = [int(n) for n in numbers]
    n_replaced = ''
    for n in num_int:
        n_replaced += ' ' + num[n]
    return n_replaced.strip()


for line in sys.stdin:
    numbers = line.strip().split(' ')
    for n in numbers:
        if len(n) < 1:
            numbers.remove(n)
    print(repl_num(numbers))
