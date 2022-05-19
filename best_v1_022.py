#!/usr/bin/env python3

import sys

def main():

    try:
        f = open(sys.argv[1], 'r')

        students = {}

        for line in f:
            tokens = line.strip().split()
            mark = int(tokens[0])
            name = ' '.join(tokens[1:])
            students[name] = mark

        max_mark = max(students, key=students.get)
        print('Best student: ' + max_mark)
        print('Best mark: ' + str(students[max_mark]))

        f.close()

    except FileNotFoundError:
        print(f'The file {sys.argv[1]} does not exist.')


if __name__ == '__main__':
    main()
