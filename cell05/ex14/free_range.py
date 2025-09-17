#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) != 2:
    print("none")
else:
    a = int(args[0])
    b = int(args[1])
    if a < b:
        print(list(range(a, b + 1)))
    else:
        print(list(range(b, a + 1)))