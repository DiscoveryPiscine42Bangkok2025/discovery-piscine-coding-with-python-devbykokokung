#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_set = set()
i = 0
while i < len(original_array):
    if original_array[i] > 5:
        new_set.add(original_array[i] + 2)
    i += 1

print(original_array)
print(new_set)