"""
Name: <Queen Hamilton, II>
<lab2>.py
"""


import math


def sum_of_threes():
    number = eval(input("Enter an upper bound: "))
    acc = 0
    for x in range(0, number + 1, 3):
        acc = acc + x
    print(acc)


def multiplication_table():
    for h in range(1, 11):
        for L in range(1, 11):
            print(h * L, end=" ")
        print("")


def triangle_area():
    a = eval(input("Enter the length of side a: "))
    b = eval(input("Enter the length of side b: "))
    c = eval(input("Enter the length of side c: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(area)


def sumSquares():
    start = eval(input("Enter a starting number: "))
    finish = eval(input("Enter an ending number: "))
    acc = 0
    for x in range(start, finish + 1):
        acc += (x * x)
    print(acc)


def power():
    base = eval(input("Enter a base number: "))
    exp = eval(input("Enter an exponent: "))
    acc = 1
    for x in range(exp):
        acc = acc * base
    print(base, "^", exp, "=", acc)


sum_of_threes()
multiplication_table()
triangle_area()
sumSquares()
power()
