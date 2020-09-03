#!/usr/bin/python3
i = range(122, 97, -2)
j = range(89, 64, -2)
cnt = 0
while cnt < 13:
    print('{:c}{:c}'.format(i[cnt], j[cnt]), end='')
    cnt = cnt + 1
