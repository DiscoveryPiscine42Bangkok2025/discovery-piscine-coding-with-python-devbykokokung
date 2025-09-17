#!/usr/bin/env python3

print("What you gotta say? : ", end='')
while True:
    response = input()
    if response == "STOP":
        break
    else :
        print("I got that! Anything else? : ", end='')