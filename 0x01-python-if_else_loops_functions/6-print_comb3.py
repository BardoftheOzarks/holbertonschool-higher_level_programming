#!/usr/bin/python3
for t in range(0, 8):
    for o in range(0, 10):
        if o > t:
            print('{}{}'.format(t, o), end=', ')
print('89')
