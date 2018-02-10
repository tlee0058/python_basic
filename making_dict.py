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

def printDict(obj):
    # print all keys and values in dictionary
    for key,value in obj.iteritems():
        print "My", key,"is", value

    #look at other ways to print dictionary
    print "\n", "---- other ways to print dictionary ----"

    #print all keys
    print "\n", "Print all keys:"
    for data in obj:
        print data

    #another way to print all keys
    print "\n", "Print all keys another way:"
    for obj_key in obj.iterkeys():
        print obj_key

    #to print the values
    print "\n", "Print all values:"
    for val in obj.itervalues():
        print val

printDict(myself)







