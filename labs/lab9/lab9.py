"""
Name: <Queen Hamilton, II>
<lab9>.py
"""


from graphics import *
import math


def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def writeSumOfSquares():
    infile = input("Enter the in-file name: ")
    outfile = input("Enter the out-file name: ")
    readfile = open(infile, "r")
    writefile = open(outfile, "w+")
    for line in readfile:
        nums = line.split()
        toNumbers(nums)
        squareEach(nums)
        summation = sumList(nums)
        writefile.write("Sum of Squares = " + str(summation))
    readfile.close()
    writefile.close()


def starter():
    weight = float(input("Enter the player's weight: "))
    numWins = int(input("Enter the number of wins the player has had: "))
    if 150 <= weight < 160 and numWins >= 5:
        print("This player should start")
    elif weight > 199 and numWins > 20:
        print("This player should start")
    else:
        print("This player should not start")


def leapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def circleOverlap():
    win = GraphWin("Circle Overlap", 500, 500)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius_1 = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, radius_1)
    c1.draw(win)
    p3 = win.getMouse()
    p4 = win.getMouse()
    radius_2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, radius_2)
    c2.draw(win)
    distance = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    if distance <= radius_1 + radius_2:
        text = Text(Point(250, 250), "The circles overlap")
    else:
        text = Text(Point(250, 250,), "The circles do not overlap")
    text.draw(win)

    win.getMouse()
    win.close()


def main():
    # add other function calls here
    starter()
    year = int(input("Enter a year: "))
    leap = leapYear(year)
    if leap:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
    circleOverlap()


main()
