"""
CTEC 121
Robert Ballenger
Module 3 Lab 1
<assignment/lab description>
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():

    """
    # conditional expressions

    # literal
    print("\nBoolean literals")
    print(True)
    print(False)
    print(type(True))
    print()

    # relational operatiors
    print("Relational operators")
    print("3 < 5", 3 < 5)
    print("3 <= 3", 3 <= 3)
    print("3 == 3", 3 == 3)
    print("3 >= 5", 3 >= 5)
    print("3 != 5", 3 != 5)
    print()

    # using variables
    x = 3
    y = 5
    print("Using variables")
    print("x:", x, "y:", y)
    print("x < y", x < y)
    print("x != y", x != y)
    print()

    # simple if statements
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")
    
    if x > y:
        print("x > y")
    
    print("end simple if example")
    print()

    # if/else statement
    print("if/else statement")
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")

    x = 6 
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")
    
    print("end if/else example")
    print()

    # Exercise 3-1
    # Have a program count from 1 to 10.
    # For each number, print a line that gives the number
    # and identifies whether the number is odd or even.


    for i in range(1, 11, 1):
        if (i % 2) == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
    print()

    # alphabetize names
    name = "Bill"
    firstLetterofName = "B"

    print("Multi-way if example")
    if firstLetterofName == "A":
        print(name)
    elif firstLetterofName == "B":
        print(name)
    elif firstLetterofName == "C":
        print(name)
    # ...
    elif firstLetterofName == "Y":
        print(name)
    else:
        print(name)
    print()
    """

    try:
        print(4/0)
    except:
        print("\nThere was a divide by zero error. Exiting\n")
        exit()
main()    