# ---------------------------------------+
# Bradley White, Chad Marks              |
# CSCI 107, Assignment 6                 |
# Last Updated: October 10, 2013         |
# ---------------------------------------| 
# This program creates three houses      |
# with varied dimensions and colors      |
# ---------------------------------------+

import turtle
import math
import random

wn = turtle.Screen()
house = turtle.Turtle()

def draw_house(start_x, start_y, some_turtle, rectangle_width, rectangle_height):

    # moves the turtle to the correct coordinates for each house
    some_turtle.up()
    some_turtle.goto(start_x, start_y)
    some_turtle.down()

    # orientates the turtle east and sets the fill color to random
    some_turtle.seth(0)
    some_turtle.fillcolor(random.random(), random.random(), random.random())
    some_turtle.begin_fill()
    
    # creates the base of the house
    for i in range(2):
        some_turtle.forward(rectangle_width)
        some_turtle.right(90)
        some_turtle.forward(rectangle_height)
        some_turtle.right(90)
        
    some_turtle.end_fill()

    # sets the fill color for the roofs to random
    some_turtle.fillcolor(random.random(), random.random(), random.random())
    some_turtle.begin_fill()

    # calculates the length of the sides of the roof and creates it
    x = (rectangle_width / 2)**2
    y = 2 * x
    
    some_turtle.left(45)
    some_turtle.forward(math.sqrt(y))
    some_turtle.right(90)
    some_turtle.forward(math.sqrt(y))

    some_turtle.end_fill()

# passes the values for each house to the function    
draw_house(0, 0, house, 100, 75)
draw_house(100, 100, house, 50, 20)
draw_house(-100, 100, house, 80, 40)        
