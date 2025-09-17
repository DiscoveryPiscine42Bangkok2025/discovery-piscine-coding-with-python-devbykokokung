#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none")
else:
    i = 1
    while i < len(sys.argv):
        match sys.argv[i].endswith("ism"):
            case False:
                print(sys.argv[i] + "ism")
        i += 1