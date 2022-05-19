#!/usr/bin/env python3

import sys

def double_v(words):
    counter = {}
    vowels = ['aa', 'ee', 'ii', 'oo', 'uu']
    for w in words:
        counter[w] = 0
    for w in words:
        current = w
        for v in vowels:
            state = v in current
            while state is True:
                #add 1 to the counter
                counter[w] += 1
                #get rid of v iside the word
                current = current.replace(v, '', 1)
                #update the state if there is no more
                if v not in current:
                    state = False
    return max(counter, key=counter.get)


words = [s.strip() for s in sys.stdin]
print(double_v(words))
#vowels = ['aa', 'ee', 'ii', 'oo', 'uu']
#for w in words:
#    current = w
#    print('-----{}----'.format(current))
#    for v in vowels:
#        print('--{}--'.format(v))
#        state = v in current
#        while state is True:
#            print(state)
#            current = current.replace(v, '', 1)
#            if not v in current:
#                state = False
#            print(current)
#    print('-------------------')
