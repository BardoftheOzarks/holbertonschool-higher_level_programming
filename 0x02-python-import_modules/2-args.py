#!/usr/bin/python3
import sys
argv = sys.argv
ac = len(argv) - 1
if ac == 1:
    print('1 argument:')
else:
    print('{:d} arguments:'.format(ac))
for i in range(1, ac + 1):
    print('{:d}: {}'.format(i, argv[i]))
