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

import random

head_counter = 0
tail_counter = 0

for i in range(1, 100):
    result = random.choice(['head', 'tail'])
    if result == "head":
        head_counter += 1
        print "Attempt #{}: Throwing a coin...It's a {}! ... Got {} head(s) so far and {} tail(s) so far". format(i, result, head_counter, tail_counter)
    elif result == "tail":
        tail_counter += 1
        print "Attempt #{}: Throwing a coin...It's a {}! ... Got {} head(s) so far and {} tail(s) so far". format(i, result, head_counter, tail_counter)
    else:
        pass
        

    





