# 1
#!/usr/bin/env python3

import requests
import random

r = requests.get('https://cat-fact.herokuapp.com/facts')

def name_calling():
    name_list = []
    for name in r.json()["all"]:
        if name.get("user"):
            name_list.append(f"{name['user']['name']['first']} {name['user']['name']['last']} is a dumb name.")
            name_set = set(name_list)
    for x in name_set:
        print(x)
name_calling()

