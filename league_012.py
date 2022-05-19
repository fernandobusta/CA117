#!/usr/bin/env python3

import sys


#we have the name of all the teams
def lookforteams(lines):
    teams = []
    scores = []
    for words in lines:
        i = 0
        while words[i].isnumeric() is False:
            i += 1
        scores.append(words[i:])
        j = 1
        current = words[0]
        while j < i:
            current = current + ' ' + words[j]
            j += 1
        teams.append(current)
    return teams, scores


#find the team with the longest string
def longest_team(teams):
    return len(max(teams, key=len))


#create the table
def table(i, current_t, current_s, long_t):
    h = i + 1
    if len(current_t) < long_t:
        spaces = long_t - len(current_t)
        first = (f'{h:3d} {current_t}') + (' ' * spaces)
    else:
        first = (f'{h:3d} {current_t}')
    second = (f'{first} {int(current_s[0]):2d}')
    current_s = current_s[1:]
    for x in current_s:
        x = int(x)
        second = second + (f'{x:4d}')
    return second


#creating the title
def title(long_t):
    space = long_t - 4
    text = ('POS CLUB ' + (' ' * space) + ' P   W   D   L  GF  GA  GD PTS')
    return text


#gathering the lines from stdin
lines = []
for line in sys.stdin:
    line = line.strip().split()
    line = line[1:]
    lines.append(line)

#variables to create the tables
teams = (lookforteams(lines)[0])
scores = (lookforteams(lines)[1])
long_t = int((longest_team(teams)))
titles = title(long_t)

#print the table
print(titles)
i = 0
while i < len(lines):
    current_t = teams[i]
    current_s = scores[i]
    print(table(i, current_t, current_s, long_t))
    i += 1
