# # Assignment: Type List
# # Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

# # Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

# # Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?

# Assignment: Compare Lists
# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

# Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]
# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]
# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']

def compare_list(list_one, list_two):
    if not len(list_one) == len(list_two):
        print "The lists are not the same"
    else:
        for i in range(0, len(list_one)):
            if not list_one[i] == list_two[i]:
                print "The lists are not the same"
                return
        print "The lists are the same"

compare_list(list_two, list_one)
