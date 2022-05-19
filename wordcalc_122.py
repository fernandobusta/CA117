#!/usr/bin/env python3

import sys

def calc(nums, variables, operants):
    try:
        sum = nums[variables[0]]
        i = 0
        while i < len(operants):
            if operants[i] == '-':
                sum -= nums[variables[i + 1]]
            elif operants[i] == '+':
                sum += nums[variables[i + 1]]
            else:
                #in case there's another operant
                #so it doesn't crash
                return operants[i]
            i += 1
        return sum

    except KeyError:
        return None


def printresult(nums, tokens, result):
    if result in nums.values():
        for key, value in nums.items():
            if value == result:
                return '{} {}'.format(' '.join(tokens[1:]), key)
    else:
        return '{} unknown'.format(' '.join(tokens[1:]))


#dict to store the values
nums = {}

for line in sys.stdin:
    tokens = line.strip().split()
    #setting commands
    if tokens[0] == 'def':
        #in case the value assigned ins't an integer
        try:
            nums[tokens[1]] = int(tokens[2])
        except ValueError:
            pass

    elif tokens[0] == 'calc':
        variables = [s for s in tokens[1:] if s.isalpha()]
        operants = [n for n in tokens[1:-1] if not n.isalpha()]
        result = calc(nums, variables, operants)
        if result in operants:
            print('The operation "{}" is not available at the moment'.format(result))
        else:
            print(printresult(nums, tokens, result))

    elif tokens[0] == 'clear':
        nums = {}

    else:
        #if the command isn't supported
        print('The command "{}" is not supported'.format(tokens[0]))
