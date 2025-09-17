#!/usr/bin/env python3

number = input("Give me a number: ")

float_num = float(number)
if float_num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")