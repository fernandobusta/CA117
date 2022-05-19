#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        x, y, n = [int(t) for t in line.strip().split()]

    for num in range(1, n + 1):
        if (num % x == 0) and (num % y == 0):
            print('fizzbuzz')
        elif num % x == 0:
            print('fizz')
        elif num % y == 0:
            print('buzz')
        else:
            print(num)


if __name__ == '__main__':
    main()
