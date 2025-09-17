#!/usr/bin/env python3

user_input = input()
result = ""

i = 0
while i < len(user_input):
    char = user_input[i]
    if char.islower():
        result += char.upper()
    elif char.isupper():
        result += char.lower()
    else:
        result += char
    i += 1

print(result)