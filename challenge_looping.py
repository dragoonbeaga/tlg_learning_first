def farms():
    global farms
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
             {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
             {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

def which_farm():
    farm = str(input(f"From which farm do you want a list of the animals?\n(1) NE Farm\n(2) W Farm\n(3)"
                     f" SE Farm\n:"))
    if farm.lower() == "ne farm":
        print(f"There are", end= ' ')
        for each_animal in farms[0]["agriculture"]:
            print(each_animal, end= ", " )
    if farm.lower() == "w farm":
        print(f"There are", end= ' ')
        for each_animal in farms[1]["agriculture"]:
            print(each_animal, end= ", " )
    else:
        print(f"There are", end=' ')
        for each_animal in farms[2]["agriculture"][0]:
            print(each_animal, end='')
farms()
which_farm()