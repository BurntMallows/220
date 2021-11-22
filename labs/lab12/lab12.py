"""
Name: <Queen Hamilton, II>
<lab12>.py
"""


from random import randint


def find_and_remove(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Queen Hamilton, II"
    except:
        pass


def read_data(filename):
    file = open(filename, "r")
    data = file.read()
    data = data.split()
    return data


def is_in_linear(search_val, values):
    var = 0
    while var < len(values):
        if search_val in values[var]:
            return True
        var += 1
    return False


def good_input():
    user_input = int(input("Enter a value (1 - 10): "))
    while not 1 <= user_input <= 10:
        print("Incorrect Input")
        if user_input > 10:
            print("Your value is too high")
        else:
            print("Your value is too low")
        user_input = int(input("Enter a value (1 - 10): "))
    return user_input


def num_digits():
    num = eval(input("Enter a positive number (0 or negative to quit): "))
    while num > 0:
        digits = 1
        while num // 10 != 0:
            num = num // 10
            digits += 1
        print("The number of digits is: {0}".format(digits))
        num = eval(input("Enter a positive number (0 or negative to quit): "))


def hi_lo_game():
    secret = randint(1, 100)
    guess = 1
    user_input = int(input("Guess a number: "))
    while user_input != secret and guess != 7:
        if user_input > secret:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        user_input = int(input("Guess a number: "))
        guess += 1
    if user_input == secret:
        print("You Win! It took you {0} guesses.".format(guess))
    else:
        print("Sorry you lost. The number was {0}.".format(secret))


def main():
    # add other function calls here
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    find_and_remove(lst, "a")
    print(lst)
    find_and_remove(lst, 7)
    print(lst)
    values = read_data("dataSorted.txt")
    print(is_in_linear("21", values))
    print(is_in_linear("14", values))
    print(good_input())
    num_digits()
    hi_lo_game()
    pass


main()
