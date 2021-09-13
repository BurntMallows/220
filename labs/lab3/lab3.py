"""
Name: <Queen Hamilton, II>
<lab3>.py
"""


def average():
    quantity = eval(input("How many grades will you enter: "))
    acc = 0
    for i in range(1, quantity + 1):
        grade = eval(input("Enter your grade on HW" + str(i) + ": "))
        acc = acc + grade
    grade_average = acc / quantity
    print(grade_average)


def tip_jar():
    acc = 0
    for i in range(1, 6):
        tip = eval(input("How much will you tip: "))
        acc = acc + tip
    print("$" + str(acc))


def newton():
    x = eval(input("Enter a value for x: "))
    refine = eval(input("Enter how many times do you want to improve the approximation: "))
    approx = x / 2
    for i in range(refine):
        approx = (approx + x / approx) / 2
    print("the square root of", x, "is", approx)


def sequence():
    term = eval(input("Enter the number of terms in the series: "))
    for i in range(1, term):
        print(1 + i // 2 * 2, end=" ")
    print()


def pi():
    n = eval(input("Enter the number of terms in the series: "))
    acc = 1
    for i in range(n):
        numerator = 2 + (i // 2 * 2)
        denominator = 1 + ((i + 1) // 2 * 2)
        fraction = numerator / denominator
        acc = acc * fraction
    print(acc * 2)


average()
tip_jar()
newton()
sequence()
pi()
