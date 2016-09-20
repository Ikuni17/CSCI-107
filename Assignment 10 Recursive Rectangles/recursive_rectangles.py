# -----------------------------------------+
# Bradley White                            | 
# CSCI 107, Assignment 10                  |
# Last Updated: November 22, 2013          |  
# -----------------------------------------|
# This is a program to recursively draw    |
# rectangles and distinguish them by color |
# -----------------------------------------+

import turtle

# function that is called to draw each rectangle
def draw_rectangle(center_x, center_y, width, height, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.speed(100)
    myTurtle.penup()
    myTurtle.goto(center_x - width/2, center_y - height/2)
    myTurtle.pendown()
    myTurtle.begin_fill()
    myTurtle.goto(center_x - width/2, center_y + height/2)
    myTurtle.goto(center_x + width/2, center_y + height/2)
    myTurtle.goto(center_x + width/2, center_y - height/2)
    myTurtle.goto(center_x - width/2, center_y - height/2)
    myTurtle.end_fill()
    
# function that calls itself to draw rectangles at each corner
# depending on the amount of levels
def rectangle_art(center_x, center_y, width, height, level, myTurtle):

    # chooses a color depending on the level
    colormap = ['orange','white','blue','green','red','yellow','violet']
    
    if (level > 0):

        draw_rectangle(center_x, center_y, width, height, colormap[level], myTurtle)

        # coordinates are adjusted until the level is less than zero
        rectangle_art(center_x + width/2, center_y - height/2, width/2,
                      height/2, level -1, myTurtle)
        rectangle_art(center_x - width/2, center_y - height/2, width/2,
                      height/2, level -1, myTurtle)
        rectangle_art(center_x - width/2, center_y + height/2, width/2,
                      height/2, level -1, myTurtle)
        rectangle_art(center_x + width/2, center_y + height/2, width/2,
                      height/2, level -1, myTurtle)      

# function to adjust the starting coordinates and amount of levels
def main():
    myTurtle = turtle.Turtle()
    myWindow = turtle.Screen()
    rectangle_art(0, 0, 200, 100, 4, myTurtle)
    myWindow.exitonclick()

main()