"""Assignment: Scores and Grades
Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A
The result should be like this:"""

import random

for i in range(10):
    rnum = random.randint(60, 100)
    
    if rnum in range(60, 70):
        print rnum, "Grade - D"
    elif rnum in range (70, 80):
        print rnum, "Grade - C"
    elif rnum in range (80, 90):
        print rnum, "Grade - B"
    else:
        print rnum, "Grade - A"
    

 



