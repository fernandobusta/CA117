#!/usr/bin/env python3

import sys

#get the order of the numbers
def bigger(num, order):
    num.sort()
    [a, b, c] = num
    final = []
    for letter in order:
        if letter == 'A':
            final.append(a)
        elif letter == 'B':
            final.append(b)
        else:
            final.append(c)
    return final


lines = []
for line in sys.stdin:
    line = line.strip()
    lines.append(line)

#splitting the input
num = lines[0].split()
#convert items in the list to integers
i = 0
while i < len(num):
    num[i] = int(num[i])
    i += 1
order = list(lines[1])

final = (bigger(num, order))
i = 0
while i < len(final):
    final[i] = str(final[i])
    i += 1
print(' '.join(final))
