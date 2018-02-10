# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

# Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?

# #input
# l = ['magical unicorns',19,'hello',98.98,'world']
# #output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"
# # input
# l = [2,3,1,7,4,12]
# #output
# "The list you entered is of integer type"
# "Sum: 29"
# # input
# l = ['magical','unicorns']
# #output
# "The list you entered is of string type"
# "String: magical unicorns"

l = ['magical unicorns',19,'hello',98.98,'world']
# if (type(l) != int):
#     print("The list you entered is a mixed type")
for items in l:
    if(type(items)== str):
        print(items)
for num in l:
    if(type(num)== int):
        print(num)
        
l1 = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical','unicorns']
l4 = [2, [55,77,33], 2.1, "end of list"]

def typeList(arr):
    sum = 0
    new_str = ""
    arrType = [0, 0, 0]
    
    for i in range(len(arr)):
        if type(arr[i]) is str:
            
            arrType[0] += 1 
            
        if type(arr[i]) is int or type(arr[i]) is float:
            sum += arr[i]
            arrType[1] += 1

    if arrType[0] == len(arr):
         print "All string"
    if arrType[1] == 
    else:
         print "mixed type"      
    

typeList(l1)
typeList(l2)
typeList(l3)
typeList(l4)
