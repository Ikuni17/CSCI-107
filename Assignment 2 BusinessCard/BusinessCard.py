# -----------------------------------------+
# Bradley White                            |
# CSCI 107, Assignment 2                   |
# Last Updated: September, 13, 2013        |
# -----------------------------------------|
# This is a program to create a custom     |
# business card based on user input.       |
# -----------------------------------------+

n = input("Please enter your name: ")
t = input("Please enter your telephone number: ")
e = input("Please enter your email address: ")
print()
print("Here is your business card ...")
print()
print("+------------------------------------------------+".ljust(50))
print("|    |                                           |".ljust(50))
print("|   -|          ".ljust(16)+n,"                    |")
print("|  --|          Tribute Liabilities Associate    |".ljust(50))
print("| ---|          Parasail Capital                 |".ljust(50))
print("| ---------                                      |".ljust(50))
print("|  -------      4 Hunger Plaza                   |".ljust(50))
print("|               STE 1400                         |".ljust(50))
print("|               District 12, Panem 00012         |".ljust(50))
print("|                                                |".ljust(50))
print("| Work: "+t,"  @: "+e,"@parasail.com    |")
print("+------------------------------------------------+".ljust(50))
