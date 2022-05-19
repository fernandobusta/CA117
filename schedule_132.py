#!/usr/bin/env python3

import sys

def sort_time(t):

    time = {}
    time_t = {}
    twelve = None

    for s in t:
        potential = s.split()[0]
        if potential[:2] == '12':
            twelve = True
            h, m = s.split(':')
            h = int(h)
            m = int(m.split()[0])
            time_t[time_to_min(h, m)] = s
        else:
            h, m = s.split(':')
            h = int(h)
            m = int(m.split()[0])
            time[time_to_min(h, m)] = s

    slist = [v for k, v in sorted(time.items())]
    tlist = [v for k, v in sorted(time_t.items())]

    if twelve is True:
        return '{}\n{}'.format('\n'.join(tlist), '\n'.join(slist))
    else:
        return '{}'.format('\n'.join(slist))


def time_to_min(h, m):
    return h * 60 + m


def main():

    try:
        times = [line.strip() for line in sys.stdin]

        #get every time in their respective am or pm cat
        am = [t for t in times if t.split()[-1] == 'a.m.']
        pm = [t for t in times if t.split()[-1] == 'p.m.']

        print(sort_time(am))
        print(sort_time(pm))

    except ValueError:
        print('Some data was incorrect')


if __name__ == '__main__':
    main()
