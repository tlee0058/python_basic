"""Assignment: Coin Tosses
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.

Sample output should be like the following:

Starting the program...
Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
...
Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
Ending the program, thank you!
Hint: Use the python built-in round function to convert that floating point number into an integer"""

def coin():
    	import random
	x = 0 
	y = 0

	for i in range (1, 51): 
		random_number = random.random()
 
		if round(random_number) == 1: 
			x = x + 1 
			print 'Attempt #' ,i, ': Throwing a coin... Its a head!... Got' ,x, 'head(s) so far and' ,y, 'tail(s) so far'
		elif round(random_number) ==0:
			y = y +1 
			print 'Attempt #' ,i, ': Throwing a coin... Its a tails!... Got' ,x, 'head(s) so far and' ,y, 'tail(s) so far'

coin()
        

    





