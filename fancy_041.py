#!/usr/bin/env python3

import sys

def read_contacts(name):

    try:
        with open(sys.argv[1], 'r') as f:
            contacts = {}
            try:
                for line in f:
                    tokens = line.strip().split()
                    contacts[tokens[0]] = (tokens[1], tokens[2])
                n = (f'Name: {name}')
                p = (f'Phone: {contacts[name][0]}')
                e = (f'Email: {contacts[name][1]}')
                return True, n, p, e

            except KeyError:
                n = (f'Name: {name}')
                return False, n, ('No such contact')

    except FileNotFoundError:
        print(f'The fiile {sys.argv[1]} does not exist')


for name in sys.stdin:
    name = name.strip()
    if read_contacts(name)[0] is True:
        print(read_contacts(name)[1])
        print(read_contacts(name)[2])
        print(read_contacts(name)[3])
    else:
        print(read_contacts(name)[1])
        print(read_contacts(name)[2])
