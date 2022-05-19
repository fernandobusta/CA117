#!/usr/bin/env python3

import sys

def main():

    try:
        with open(sys.argv[1], 'r') as f:

            students = {}
            #store the names and marks in a dict
            for line in f:
                tokens = line.strip().split()
                mark = int(tokens[0])
                students[tokens[0]] = ' '.join(tokens[1:])
            #find the highest mark
            maxm = max(students, key=students.get)
            print('Best student: ' + mark)
            print('Best mark: ' + str(students[maxm]))

    except ValueError:
        print(f'Invalid mark {tokens[0]} encountered. Exiting.')
    except FileNotFoundError:
        print(f'The file {sys.argv[1]} does not exist.')


if __name__ == '__main__':
    main()
