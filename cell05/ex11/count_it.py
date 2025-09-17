#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    print("parameters: " + str(len(args)))
    
    for arg in args:
        print(arg + ": "+ str(len(arg)))