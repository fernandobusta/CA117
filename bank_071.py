#!/usr/bin/env python3

class BankAccount(object):

    def set_attributes(b, name, number, balance):
        b.name = name
        b.number = number
        b.balance = float(balance)

    def print_attributes(b):
        print(f'Name: {b.name}')
        print(f'Account number: {b.number}')
        print(f'Balance: {b.balance:.2f}')

    def deposit(b, n):
        b.balance += n
