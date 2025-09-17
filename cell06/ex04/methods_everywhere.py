#!/usr/bin/env python3

import sys

def shrink(message):
    print(message[slice(8)])

def enlarge(message):
    while len(message) < 8:
        message += "Z"
    print(message)

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    i = 0
    while i < len(args):
        if len(args[i]) < 8:
            enlarge(args[i])
        elif len(args[i]) > 8:
            shrink(args[i])
        else:
            print(args[i])
        i += 1