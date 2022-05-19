#!/usr/bin/env python3

import sys

def cuadrant(x, y):
   if x < 0:
      if y < 0:
         return 3
      return 4
   else:
      if y < 0:
         return 2
      return 1


for line in sys.stdin:
   x, y = line.strip().split()
   print(cuadrant(int(x), int(y)))
