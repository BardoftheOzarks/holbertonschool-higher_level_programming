#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    ac = len(argv) - 1
    if ac == 0:
        print('{} arguments.'.format(ac))
    elif ac == 1:
        print('{} argument:'.format(ac))
        print('{}: {}'.format(ac, argv[ac]))
    else:
        print('{} arguments:'.format(ac))
        for i in range(1, ac + 1):
            print('{}: {}'.format(i, argv[i]))
