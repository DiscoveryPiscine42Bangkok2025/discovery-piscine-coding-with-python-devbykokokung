#!/usr/bin/env python3

def famous_births(persons_dict):
    i = 0
    dict_lists = sorted(persons_dict.values(), key=lambda x: int(x["date_of_birth"]))
    while i < len(dict_lists):
        print(f"{dict_lists[i]['name']} is a great scientist born in {dict_lists[i]['date_of_birth']}.")
        i += 1

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)