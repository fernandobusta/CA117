#!/usr/bin/env python3

def maximum(m, current_max=None):
    if not m:
        return current_max
    potential = m.pop()
    if current_max is None or current_max < potential:
        return maximum(m, potential)
    return maximum(m, current_max)
