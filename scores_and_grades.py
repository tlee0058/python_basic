"""Assignment: Scores and Grades
Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A
The result should be like this:"""

import random


for i in range(11):
    random_num = int(random.random()*100)
    if random_num in range(60, 70):
        print "Score: {}; Your grade is B".format(random_num)
    elif random_num in range(70, 80):
        print "Score: {}; Your grade is C".format(random_num)
    elif random_num in range(80, 90):
        print "Score: {}; Your grade is B".format(random_num)
    elif random_num in range(90, 100):
        print "Score: {}; Your grade is A".format(random_num)
    else:
        print "below D"


    
def grade(score):
    letter = "F"
    if (score >= 90):
        letter = "A"
    elif (score >= 80):
        letter = "B"
    elif (score >= 70):
        letter = "C"
    elif (score >= 60):
        letter = "D"
    return letter

import random
for i in range(10):
    random_num = random.randrange(100)
    gr = grade(random_num )
    print "Score: ", random_num, " ; Your grade is", gr
print "End of the program. Bye!"




