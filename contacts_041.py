#!/usr/bin/env python3

import sys

def read_contacts(name):

    try:

        with open(sys.argv[1]) as f:
            contacts = {}
            try:
                for line in f:
                    tokens = line.strip().split()
                    contacts[' '.join(tokens[:-1])] = tokens[-1]
                n = (f'Name: {name}')
                p = (f'Phone: {contacts[name]}')

                return True, n, p

            except KeyError:
                n = (f'Name: {name}')
                return False, ('No such contact'), n

    except FileNotFoundError:
        (f'The file {sys.arv[1]} does not exist.')


for name in sys.stdin:
    name = name.strip()

    if read_contacts(name)[0] is True:
        print(read_contacts(name)[1])
        print(read_contacts(name)[2])
    else:
        print(read_contacts(name)[2])
        print(read_contacts(name)[1])
