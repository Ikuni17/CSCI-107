#------------------------------------------------+
# Bradley White                                  |
# CSCI 107, Assignment 5                         |
# Last Updated: October 4, 2013                  |
#------------------------------------------------|
# This is a program to creates three houses      |
# with random colors within a neighborhood       |
#------------------------------------------------+

import turtle
import random
house = turtle.Turtle()

# moves the turtle west to allow space for three houses
house.up()
house.goto(-175,0)
house.down()

# loop to create three houses
for houses in range(3):

    house.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    house.begin_fill()

    # creates the random colored base
    for side in range(2):
        house.forward(100)
        house.right(90)
        house.forward(75)
        house.right(90)
     
    house.end_fill()
    house.left(60)

    house.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    house.begin_fill()

    # creates the random colored roof
    for side in range(3):
        house.forward(100)
        house.right(120)
        
    house.end_fill()

    # moves to the next house
    house.up()
    house.right(60)
    house.forward(125)
    house.down()
