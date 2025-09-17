#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) < 2:
    print("none")
else:
    i = len(args) - 1
    while i >= 0:
        print(args[i])
        i -= 1