#!/usr/bin/env python3

number = int(input("Enter a number\n"))

i = 0
while i < 10:
    result = number * i
    print(f"{i} x {number} = {result}")
    i += 1