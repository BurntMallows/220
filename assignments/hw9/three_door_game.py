"""
Name: <Queen Hamilton, II>
<three_door_game>.py

Problem: This program creates a three door game

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


from random import randint
from graphics import Text, Rectangle, GraphWin, Point
from button import Button


def draw_text(text, point, win):
    message = Text(point, text)
    message.draw(win)
    return message


def draw_door(point_1, point_2, label, win):
    box = Rectangle(point_1, point_2)
    door = Button(box, label)
    door.draw(win)
    return door


def main():
    win = GraphWin("Three Door Game", 700, 500)
    win.setCoords(0, 0, 20, 20)
    secret = draw_text("I have a secret door", Point(10, 15), win)

    door_1 = draw_door(Point(2, 9), Point(5, 12), "Door1", win)
    door_2 = draw_door(Point(8.5, 9), Point(11.5, 12), "Door2", win)
    door_3 = draw_door(Point(15, 9), Point(18, 12), "Door3", win)
    num = randint(1, 3)

    bottom_text = draw_text("Click to choose my door", Point(10, 2), win)
    click_door = 0
    while not click_door:
        point = win.getMouse()
        if door_1.is_clicked(point):
            click_door = 1
            door = door_1
        elif door_2.is_clicked(point):
            click_door = 2
            door = door_2
        elif door_3.is_clicked(point):
            click_door = 3
            door = door_3
        else:
            click_door = 0

    secret.undraw()
    bottom_text.setText("Click anywhere to close")

    if click_door == num:
        door.color_button("green")
        draw_text("You Win!", Point(10, 15), win)
    else:
        door.color_button("red")
        draw_text("You Lost!", Point(10, 15), win)
        draw_text("Door{0} is my secret door".format(num), Point(10, 14), win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
