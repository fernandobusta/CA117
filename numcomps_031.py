#!/usr/bin/env python3

import sys


def table(n):
    m_three = [n for n in range(n + 1) if not n % 3]
    s_three = [n * n for n in m_three]
    d_four = [n * 2 for n in range(n + 1) if not n % 4]
    m_three_or_four = [n for n in range(n + 1) if not n % 4 or not n % 3]
    m_three_and_four = [n for n in range(n + 1) if not n % 4 and not n % 3]
    return m_three, s_three, d_four, m_three_or_four, m_three_and_four


for line in sys.stdin:
    n = int(line.strip())
    lists = table(n)
    fixed = []
    i = 0
    while i < len(lists):
        current = lists[i]
        if 0 in current:
            current.pop(0)
        fixed.append(current)
        i += 1

    #print the results
    print(f'Multiples of 3: {fixed[0]}')
    print(f'Multiples of 3 squared: {fixed[1]}')
    print(f'Multiples of 4 doubled: {fixed[2]}')
    print(f'Multiples of 3 or 4: {fixed[3]}')
    print(f'Multiples of 3 and 4: {fixed[4]}')
