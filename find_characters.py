
# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

# Here's an example:

# # input
# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# # output
# new_list = ['hello','world']

word_list = ['hello','world','my','name','is','Anna']
char = 'o'

for items in word_list:
    for letter in items:
        if(letter == char):
            print (items)
