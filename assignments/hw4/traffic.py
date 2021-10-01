"""
Name: Queen Hamilton, II
<traffic>.py

Problem: This program calculates traffic patterns from input

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def main():
    # ask for input: how many roads were surveyed?
    roads = eval(input("How many roads were surveyed? "))
    # set total accumulator
    total = 0
    # ask for input: how many days was road x surveyed?
    for loop in range(1, roads + 1):
        days = eval(input("How many days was road " + str(loop) + " surveyed? "))
        # set daily accumulator
        acc = 0
        # ask for input: how many cars traveled on day y? and add
        for i in range(1, days + 1):
            cars = eval(input("     How many cars traveled on day " + str(i) + "? "))
            acc = acc + cars
        # calculate total
        total = total + acc
        # calculate average per day for each road and print
        road_average = acc / days
        print("Road", loop, "average vehicles per day:", round(road_average, 2))
    # calculate the average amount of cars for all the roads
    total_average = total / roads
    # print total and total average
    print("Total number of vehicles traveled on all roads:", total)
    print("Average number of vehicles per road:", round(total_average, 2))


if __name__ == "__main__":
    main()
