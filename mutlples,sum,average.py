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
#Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

# for i in range(1,1001):
#     if i % 2 !=0:
#         print (i)

# #Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
# for i in range(1,1001,5):
#     print(i)

#Sum List
#Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

a = [1, 2, 5, 10, 255, 3]
print (sum(a))

average = sum(a)/len(a)
print (average)


#Average List
#Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
