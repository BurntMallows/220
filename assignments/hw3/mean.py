"""
Name: Queen Hamilton, II
<mean>.py

Problem: This program calculates RMS, Harmonic, and Geometric averages

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


# 1. What will the program do: It will calculate and display the rms average, harmonic mean,
# and geometric mean of a set of numbers that a user enters
# 2. What will be the inputs and outputs: The input will be a list of numbers. The outputs will be
# the calculated RMS average, Harmonic mean, and Geometric mean.
# 3. What is a step by step list of what the program must do
# I did this step but I like to write my code under the relative pseudo-code line


# import math
import math


def main():
    # Ask for user input regarding value quantity
    variable = eval(input("Enter the values to be entered: "))
    # set accumulators
    acc = 0
    acc2 = 0
    acc3 = 1
    # Ask for value input as for many times as they specified
    for _ in range(variable):
        number = eval(input("Enter value: "))
        # rms - add the squared values together
        acc = acc + number ** 2
        # harmonic - add the values' reciprocals
        acc2 = acc2 + 1 / number
        # geometric - multiply the values
        acc3 = acc3 * number
    # rms - find the mean by dividing the sum by the entered quantity
    mean = acc / variable
    # square the mean to find the rms average
    rms_average = round(math.sqrt(mean), 3)
    # harmonic - divide number of values by the sum of the reciprocals
    harmonic_mean = round(variable / acc2, 3)
    # geometric - raise the product of 1 / the number of values
    geometric_mean = round(acc3 ** (1 / variable), 3)
    # print the averages
    print(rms_average)
    print(harmonic_mean)
    print(geometric_mean)


# call the function
if __name__ == "__main__":
    main()
