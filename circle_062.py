#!/usr/bin/env python3

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    dist1 = x2 - x1
    dist2 = y2 - y1
    dist_total = dist1 * dist1 + dist2 * dist2
    if dist_total < (r1 + r2)**2:
        #and dist_total < (r1 * 2 + r2 * 2)**2:
        return True
    else:
        return False
