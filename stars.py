"""Assignment: Stars
Write the following functions.

Part I
Create a function called draw_stars() that takes a list of numbers and prints out *.

For example:

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x) should print the following when invoked:"""

x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(x):
    star = "*"
    for i in x:
        i *= star
        print i

draw_stars(x)

        

    





