"""Assignment: Making Dictionaries
Create a function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values. Assume the lists will be of equal length.

Your first function will take in two lists containing some strings. Here are two example lists:
"""
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

# comboList = zip(name, favorite_animal)


# new_dict = dict(comboList)
# print new_dict

def make_dict(list1, list2):
    new_dict = {}
    for i in list1:
        pass
    for j in list2:
        pass
    new_dict.fromkeys(i, [j])

    print new_dict

make_dict(name, favorite_animal)







