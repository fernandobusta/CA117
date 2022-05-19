#!/usr/bin/env python3

import sys

def main():

    try:

        with open(sys.argv[1], 'r') as f:

            students = {}
            #store the names and marks on a dict
            for line in f:

                try:

                    tokens = line.strip().split()
                    mark = int(tokens[0])
                    students[' '.join(tokens[1:])] = mark
                except ValueError:
                    print(f'Invalid mark {tokens[0]} encountered. Skipping.')

            #find the highest mark
            maxm = max(students, key=students.get)
            print('Best student: ' + str(maxm))
            print('Best mark: ' + str(students[maxm]))

    except FileNotFoundError:
        print(f'The file {sys.argv[1]} does not exist.')


if __name__ == '__main__':
    main()
