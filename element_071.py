#!/usr/bin/env python3

class Element(object):

    def set_attributes(e, number, name, symbol, bp):
        e.number = number
        e.name = name
        e.symbol = symbol
        e.bp = bp

    def print_attributes(e):
        print(f'Number: {e.number}')
        print(f'Name: {e.name}')
        print(f'Symbol: {e.symbol}')
        print(f'Boiling point: {e.bp} K')
