
# Assignment: Checkerboard
# Write a program that prints a 'checkerboard' pattern to the console.

# Your program should require no input and produce console output that looks like so:

# Each star or space represents a square. On a traditional checkerboard you'll see alternating squares of red or black. In our case we will alternate stars and spaces. The goal is to repeat a process several times. This should make you think of looping.

box = "* * * *"
box2 = " * * * *"
for square in range(0, 7):
    if square % 2 == 0:
        print(box)
    if square % 2 != 0:
        print(box2)
