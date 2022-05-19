#!/usr/bin/env python3

import sys

def translation(num):
    try:
        t = {}
        with open(sys.argv[1], 'r') as f:
            i = 0
            for line in f:
                tokens = line.split()
                t[i] = tokens[1]
                i += 1

        translated = [t[n] for n in num]
        translated = ' '.join(translated)
        return translated
    except FileNotFoundError:
        print(f'The file {sys.argv[1]} does not exist')


numbers = []
for line in sys.stdin:
    numbers = line.strip().split(' ')
    for n in numbers:
        if n == '':
            numbers.remove(n)
    num = [int(n) for n in numbers]
    print(translation(num))
