# -----------------------------------------------+
# Bradley White                                  | 
# CSCI 107, Assignment 9                         |
# Last Updated: November 8, 2013                 |  
# -----------------------------------------------|
# This is a program to calculate pascal's        |
# triangle and sets the numbers within a custom  |
# field width; to allow for larger triangles     |
# -----------------------------------------------+

def pascal_triangle(total_rows, field_width):

    # string to remember the calculated numbers in each row
    r = ""

    # loop for each row of the triangle defined by the user
    for row in range(total_rows):

        # sets number back to 1 at the beginning of each row and adds it the r string
        number = 1
        r += str(number).center(field_width)

        # formula to calculate each row of Pascal's depending on row number and the previous
        # number within that row. Then the number is placed in the r string and the loop continues
        for sequence in range(row):
            number = int(number * (row-sequence) * 1 / (sequence + 1))
            r += str(number).center(field_width)

        # prints the r string after the loop has finished, and then clears it before the next row is calculated
        print(r.center(field_width * total_rows))
        r = ""

# start!
pascal_triangle(12, 6)
