#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    string = sys.argv[1]
    z_found = False
    i = 0
    while i < len(string):
        if string[i].lower() == 'z':
            print("z", end="")
            z_found = True
        i += 1
    if z_found:
        print()
    else:
        print("none")