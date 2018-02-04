"""Find and Replace
In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".

Min and Max
Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

First and Last
Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.

New List
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!"""

# words = "It's thanksgiving day. It's my birthday, too!"

# Assignment: Multiples, Sum, Average
#This assignment has several parts. All of your code should be in one file that is well commented to indicate what each block of code is doing and which problem you are solving. Don't forget to test your code as you go!#

#Multiples

# Python / Django Online Python Fundamentals v1.1 Python Fundamentals Filter by Type Ting Hello,  Ting L  
# CHECKLIST
# MandatoryDeadline: Monday of Week 1Difficulty Level: BasicEstimated Time: 30min
# Assignment: Filter by Type
# Write a program that, given some value, tests that value for its type. Here's what you should do for each type:

# Integer
# If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"

# String
# If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."

# List
# If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."

# Test your program using these examples:

x = 45
if x >= 100:
    print ("That's a big number")

if x < 100:
    print ("That a small number")
y = "hello world how are yall"
if len(y) >= 50:
    print ("Long Sentence")
if len(y) < 50:
    print ("short sentence")

lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
if len(lL) >= 10:
    print("Big List!")
if len(lL) < 10:
    print("Short List")
