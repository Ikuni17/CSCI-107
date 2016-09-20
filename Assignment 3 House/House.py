#------------------------------------------------+
# Bradley White                                  |
# CSCI 107, Assignment 3                         |
# Last Updated: September 18, 2013               |
#------------------------------------------------|
# This is a program to create a blue house with  |
# a red roof, and a yellow garage on the side    |
#------------------------------------------------+

import turtle
wn = turtle.Screen()
house = turtle.Turtle()

house.up()
house.goto(-50,0)
house.down()

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

house.up()
house.goto(-50, -75)
house.down()

house.fillcolor("yellow")
house.begin_fill()

house.forward(50)     #creates the yellow garage
house.right(90)
house.forward(50)
house.right(90)
house.forward(50)
house.right(90)
house.forward(50)

house.end_fill()