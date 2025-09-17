#!/usr/bin/env python3

number = int(input("Enter a number less than 25\n"))

if  number > 25:
    print("Error")
else :
    i = number
    while i <= 25:
        print(f"Inside the loop, my variable is {i}")
        i += 1