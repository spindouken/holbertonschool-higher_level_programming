#!/usr/bin/python3
for x in range(10):
    for z in range(10):
        if z <= x:
            continue
        elif z != 9:
            print('{}{}'.format(x, z), end=", ")
        else:
            print('{}{}'.format(x, z))
