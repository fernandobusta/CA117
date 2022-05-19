#!/usr/bin/env python3

def minimum(m, current_min=None):

    #if len(m) == 1:
        #return m

    #search which of the 2 lat
    #parameters is smaller
    #if m[0] < m[1]:
    #remove m[1]
        #return minimum(m.remove(m[1]))
    #remove m[0]
    #return minimum(m.remove(m[0]))
    if not m:
        return current_min
    potential = m.pop()
    if current_min is None or potential < current_min:
        return minimum(m, potential)
    return minimum(m, current_min)
