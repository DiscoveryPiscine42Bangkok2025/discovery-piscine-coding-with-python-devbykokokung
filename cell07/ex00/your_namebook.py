#!/usr/bin/env python3

def array_of_names(persons_dict):
    dict_lists = list(persons_dict.items())
    i = 0
    while i < len(dict_lists):
        dict_lists[i] = dict_lists[i][0].capitalize() + " " + dict_lists[i][1].capitalize()
        i += 1
    return dict_lists

persons = {
 "jean": "valjean",
 "grace": "hopper",
 "xavier": "niel",
 "fifi": "brindacier"
}

print(array_of_names(persons))