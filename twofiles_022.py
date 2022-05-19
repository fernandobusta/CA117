#!/usr/bin/env python3

import sys

def main():

    try:

        with open(sys.argv[1], 'r') as f:

            a = []
            for line in f:
                a.append(line.strip())

    except FileNotFoundError:
        print(f'The file {sys.argv[0]} does not exist')

    try:

        with open(sys.argv[2], 'r') as g:

            b = []
            for line in g:
                b.append(line.strip())

    except FileNotFoundError:
        print(f'The file {sys.argv[1]} does not exist')

    ab = []
    i = 0
    while i < len(a):
        ab.append(a[i])
        ab.append(b[i])
        i += 1

    for n in ab:
        print(n)


if __name__ == '__main__':
    main()
