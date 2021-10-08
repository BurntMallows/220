"""
Name: <Queen Hamilton, II>
<greeting>.py

Problem: This program animates a Valentine's day card

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


from graphics import GraphWin, Line, Point, Polygon, Text, update


def main():
    win = GraphWin("Valentine's Card", 500, 500, autoflush=False)
    win.setCoords(0, 0, 20, 20)

    arrow = Line(Point((-7), 11.5), Point(0, 11.5))
    arrow.setArrow("last")
    arrow.draw(win)
    line_a = Line(Point((-7.5), 11.75), Point((-7), 11.5))
    line_a.draw(win)
    line_b = Line(Point((-7.5), 11.25), Point((-7), 11.5))
    line_b.draw(win)

    heart = Polygon(Point(10, 8), Point(8, 10), Point(7, 12), Point(7, 13), Point(8, 14),
                    Point(9.65, 14),Point(10, 13.45), Point(10.35, 14), Point(12, 14),
                    Point(13, 13), Point(13, 12), Point(12, 10))
    heart.setFill("pink")
    heart.setOutline("black")
    heart.draw(win)

    happy = Text(Point(10, 16), "H A P P Y")
    happy.setSize(30)
    happy.setStyle("bold")
    happy.setFace("courier")
    happy.setTextColor("red")
    happy.draw(win)

    valentines = Text(Point(10, 6), "V A L E N T I N E S")
    valentines.setSize(25)
    valentines.setStyle("bold")
    valentines.setFace("courier")
    valentines.setTextColor("red")
    valentines.draw(win)

    for _ in range(9):
        arrow.move(1.5, 0)
        line_a.move(1.5, 0)
        line_b.move(1.5, 0)
        update(3)

    close = Text(Point(10, 2), "Click anywhere to close")
    close.draw(win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
