"""
Name: <Queen Hamilton, II>
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter how many shots were taken: "))
    shots_made = eval(input("Enter how many shots were made: "))
    percentage = shots_made / total_shots * 100
    print("Your shoot percentage is", percentage, "%")


def coffee():
    pounds = eval(input("Enter how many pounds of coffee are being ordered: "))
    cost = pounds * (10.50 + 0.86) + 1.50
    print("The total cost of your order is: $", cost)


def kilometers_to_miles():
    kilometers = eval(input("Enter number of kilometers: "))
    miles = kilometers / 1.61
    print(kilometers, "kilometers =", miles, "miles")


calc_rec_area()
calc_volume()
shooting_percentage()
coffee()
kilometers_to_miles()
