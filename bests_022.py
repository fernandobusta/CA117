#!/usr/bin/env python3

import sys

def main():

    try:

        with open(sys.argv[1], 'r') as f:

            students = {}
            samegrade = {}
            #store the names and marks on a dict
            for line in f:

                try:

                    tokens = line.strip().split()
                    mark = int(tokens[0])
                    students[' '.join(tokens[1:])] = mark

                except ValueError:
                    print(f'Invalid mark {tokens[0]} encountered. Skipping.')

            max_st_01 = max(students, key=students.get)
            max_mark = (students[max_st_01])

            high_st = []
            for s in students.keys():
                if int(students[s]) == max_mark:
                    high_st.append(s)

            print('Best student(s): ' + ', '.join(high_st))
            print('Best mark: ' + str(max_mark))

    except FileNotFoundError:
        print(f'The file {sys.argv[1]} does not exist')


if __name__ == '__main__':
    main()
