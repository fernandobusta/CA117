#!/usr/bin/env python3

import sys

def censor(line):
    try:
        words = []
        with open(sys.argv[1], 'r') as f:
            #get the censoring words
            for s in f:
                words.append(s.strip())

        #replace censored words on lower case version of line
        line_lower = line.lower()
        i = 0
        while i < len(words):
            line_lower = line_lower.replace(words[i], '@' * len(words[i]))
            i += 1
        #find positions of ampersand in line
        positions = []
        i = 0
        while i < len(line):
            if line_lower[i] == '@':
                positions.append(i)
            i += 1
        #replace it in the original version of line
        i = 0
        new = ''
        while i < len(line):
            if i in positions:
                new = new + '@'
            else:
                new = new + line[i]
            i += 1
        return new

    except FileNotFoundError:
        print(f'The file {sys.arv[2]} does not exist')


for line in sys.stdin:
    line = line.strip()
    print(censor(line))
