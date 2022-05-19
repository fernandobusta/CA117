#!/usr/bin/env python3

import sys

def dnum():
    num = {0: 'zero',
           1: 'one',
           2: 'two',
           3: 'three',
           4: 'four',
           5: 'five',
           6: 'six',
           7: 'seven',
           8: 'eight',
           9: 'nine',
           10: 'ten',
           11: 'eleven',
           12: 'twelve',
           13: 'thirteen',
           20: 'twenty',
           30: 'thirty',
           40: 'forty',
           50: 'fifty',
           80: 'eighty',
           100: 'one hundred'}
    return num


def conversion(num, serie):
    t = []
    for n in serie:
        if n in num:
            t.append(num[n])
        elif n < 20:
            n = str(n)
            if int(n[1]) == 8:
                word = num[int(n[1])] + 'een'
            else:
                word = num[int(n[1])] + 'teen'
            t.append(word)
        else:
            #n < 100:
            n = str(n)
            if int(n[0]) > 5 and int(n[0]) != 8:
                if int(n[1]) == 0:
                    word = num[int(n[0])] + 'ty'
                else:
                    word = num[int(n[0])] + 'ty' + '-' + num[int(n[1])]
                t.append(word)
            else:
                h = int(n[0]) * 10
                word = num[h] + '-' + num[int(n[1])]
                t.append(word)
    return ' '.join(t)


for line in sys.stdin:
    serie = [int(n) for n in line.strip().split()]
    num = dnum()
    print(conversion(num, serie))
