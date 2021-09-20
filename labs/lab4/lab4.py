"""
Name: <Queen Hamilton, II>
<lab4>.py
"""

from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to create a square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(40, 40), Point(60, 60))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to create new squares
    for i in range(num_clicks):
        p = win.getMouse()

        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    close = Text(Point(200, 100), "Click again to quit")
    close.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    # builds a rectangle
    win = GraphWin("Rectangle", 400, 400)
    point1 = win.getMouse()
    point2 = win.getMouse()
    box = Rectangle(point1, point2)
    box.draw(win)

    # calculates perimeter and area
    width = point2.getX() - point1.getX()
    length = point2.getY() - point1.getY()
    perimeter = abs(width * 2 + length * 2)
    area = abs(width * length)

    # final texts
    perimeter_text = Text(Point(200, 350), "The perimeter of your rectangle is: " + str(perimeter))
    area_text = Text(Point(200, 375), "The area of your rectangle is: " + str(area))
    close = Text(Point(200, 100), "Click again to quit")
    perimeter_text.draw(win)
    area_text.draw(win)
    close.draw(win)
    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 400, 400)
    center = win.getMouse()
    circumference_point = win.getMouse()
    x1 = center.getX()
    x2 = circumference_point.getX()
    y1 = center.getY()
    y2 = circumference_point.getY()
    radius = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    spiral = Circle(center, radius)
    spiral.draw(win)
    radius_text = Text(Point(200, 350), "The radius of your circle is: " + str(radius))
    close = Text(Point(200, 100), "Click again to quit")
    radius_text.draw(win)
    close.draw(win)
    win.getMouse()
    win.close()


def pi2():
    n = eval(input("Enter the number of terms to sum: "))
    acc = 0
    for i in range(n):
        numerator = 4
        denominator = 1 + 2 * i
        fraction = (numerator / denominator) * ((-1) ** i)
        acc = acc + fraction
    print(acc)
    print(math.pi - acc)
    pass


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()