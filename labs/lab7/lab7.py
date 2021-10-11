"""
Name: <Queen Hamilton, II>
<lab7>.py
"""


import math


def cash_conversion():
    integer = int(input("Enter an integer: "))
    print("$" + "{:.2f}".format(integer))


def encode():
    message = input("Enter a message to be encoded: ")
    key = int(input("Enter an integer key value: "))
    acc = ""
    for i in message:
        x = ord(i)
        number = chr(key + x)
        acc = acc + number
    print(acc)


def sphere_area(radius):
    surface_area = 4 * math.pi * radius ** 2
    return surface_area


def sphere_volume(radius):
    volume = 4 / 3 * math.pi * radius ** 3
    return volume


def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total


def sum_n_cubes(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i ** 3
    return total


def encode_better():
    message = input("Enter a message to encode: ")
    key = input("Enter a key: ")
    acc = ""
    for i in range(len(message)):
        nums = ord(message[i])
        k = ord(key[i])
        evaluate = nums + k - 97
        acc = acc + chr(evaluate)
    print(acc)


def main():
    # add function calls here
    cash_conversion()
    encode()
    radius = float(input("Enter the radius of a sphere: "))
    print("The surface area is:", sphere_area(radius))
    print("The volumes is:", sphere_volume(radius))
    n = int(input("Enter the number of times to loop: "))
    print(sum_n(n))
    print(sum_n_cubes(n))
    encode_better()
    pass


main()
