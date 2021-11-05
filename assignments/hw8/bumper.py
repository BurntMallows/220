"""
Name: <Queen Hamilton, II>
<bumper>.py

Problem: This program models random collision behavior using circles

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


import math
from random import randint
from graphics import color_rgb, GraphWin, Circle, Point, update, Text


def get_random(move_amount):
    side_x, side_y = 0, 0
    while (side_x + side_y) == 0:
        side_x = randint(-move_amount, move_amount)
        side_y = randint(-move_amount, move_amount)
    return side_x, side_y


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = color_rgb(red, green, blue)
    return color


def draw_ball(num, win):
    x_max = win.getWidth() - num
    y_max = win.getHeight() - num
    ball = Circle(Point(randint(num, x_max), randint(num, y_max)), num)
    ball.setFill(get_random_color())
    ball.draw(win)
    return ball


def get_click(win):
    try:
        click = win.checkMouse()
        return click.getX() >= 0
    except AttributeError:
        return False


def did_collide(ball_a, ball_b):
    center_1 = ball_a.getCenter()
    center_2 = ball_b.getCenter()
    distance = math.sqrt((center_1.getX() - center_2.getX()) ** 2 +
                         (center_1.getY() - center_2.getY()) ** 2)
    radii = ball_a.getRadius() + ball_b.getRadius()
    return distance <= radii


def hit_horizontal(ball, win):
    center_p = ball.getCenter()
    distance_l = math.sqrt((center_p.getX() - 0) ** 2)
    distance_r = math.sqrt((center_p.getX() - win.getWidth()) ** 2)
    return distance_l <= ball.getRadius() or distance_r <= ball.getRadius()


def hit_vertical(ball, win):
    center_p = ball.getCenter()
    distance_b = math.sqrt((center_p.getY() - 0) ** 2)
    distance_t = math.sqrt((center_p.getY() - win.getHeight()) ** 2)
    return distance_b <= ball.getRadius() or distance_t <= ball.getRadius()


def main():
    win = GraphWin("Bumper", 500, 500, autoflush=False)
    ball_a = draw_ball(25, win)
    ball_b = draw_ball(25, win)
    center_1, radius_1 = get_random(25)
    center_2, radius_2 = get_random(25)
    click = get_click(win)
    while not click:
        hit_h1 = hit_horizontal(ball_a, win)
        hit_h2 = hit_horizontal(ball_b, win)
        hit_ball = did_collide(ball_a, ball_b)
        if hit_h1 or hit_ball:
            center_1 = -center_1
        if hit_h2 or hit_ball:
            center_2 = -center_2
        hit_v1 = hit_vertical(ball_a, win)
        hit_v2 = hit_vertical(ball_b, win)
        if hit_v1 or hit_ball:
            radius_1 = -radius_1
        if hit_v2 or hit_ball:
            radius_2 = -radius_2
        update(8)
        ball_a.move(center_1, radius_1)
        ball_b.move(center_2, radius_2)

        click = get_click(win)

    close = Text(Point(250, 100), "Click anywhere to close")
    close.draw(win)
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
