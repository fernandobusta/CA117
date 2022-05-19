#!/usr/bin/env python3

import sys

def game(start, seq):
    current = start
    for mov in seq:
        if mov == 'A':
            if current == 1:
                current = 2
            elif current == 2:
                current = 1
            else:
                #current = 3
                pass
        elif mov == 'B':
            if current == 2:
                current = 3
            elif current == 3:
                current = 2
            else:
                #current = 1
                pass
        else:
            #mov = C
            if current == 1:
                current == 3
            elif current == 3:
                current == 1
            else:
                #current = 2
                pass
    return current


tokens = []
for line in sys.stdin:
    tokens.append(line.strip())
start = int(tokens[0])
seq = [s for s in tokens[1]]
print(game(start, seq))
