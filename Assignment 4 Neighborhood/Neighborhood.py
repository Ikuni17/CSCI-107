#------------------------------------------------+
# Bradley White                                  |
# CSCI 107, Assignment 4                         |
# Last Updated: September 23, 2013               |
#------------------------------------------------|
# This is a program to create three blue houses, |
# with red roofs within a neighborhood.          |
#------------------------------------------------+

import turtle
wn = turtle.Screen()
house = turtle.Turtle()

house.up()
house.goto(-175,0)
house.down()

for i in range(3):
    house.fillcolor("blue")
    house.begin_fill()

    house.forward(100)    #creates the blue house
    house.right(90)
    house.forward(75)
    house.right(90)
    house.forward(100)
    house.right(90)
    house.forward(75)

    house.end_fill()

    house.fillcolor("red")
    house.begin_fill()

    house.right(30)       #creates the red roof
    house.forward(100)
    house.right(120)
    house.forward(100)
    house.right(120)
    house.forward(100)

    house.end_fill()

    house.up()            #moves to the next house
    house.right(180)
    house.forward(125)
    house.down()