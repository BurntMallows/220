"""
Name: <Queen Hamilton, II>
<lab11>.py
"""


from random import randint
from graphics import *


def words(file):
    infile = open(file, "r")
    contents = infile.read()
    return contents.split("\n")


def random_word(file_contents):
    return file_contents[randint(0, len(file_contents) - 1)]


def fill(word, letters):
    secret = ["_"] * len(word)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return "".join(secret)


def won(word, letters):
    secret = fill(word, letters)
    return secret == word


def play():
    w = words("wordlist.txt")
    word = random_word(w)
    incorrect = 0
    guesses = []
    current = "_" * len(word)
    while incorrect != 7 and not won(word, current):
        display = fill(word, guesses)
        print(display)
        print(guesses)
        letter = input("Guess a letter: ")
        while letter in guesses:
            letter = input("Guess a letter: ")
        guesses.append(letter)
        display = fill(word, guesses)
        if display == current:
            incorrect += 1
        else:
            current = display
    if incorrect == 7:
        print("Better luck next time!\nThe word was: {0}".format(word))
    else:
        print("{0}\nCongratulations!! You win!".format(word))


# def graphics_display():
#     win = GraphWin("Hangman", 500, 500)
#     win.setCoords(0, 0, 20, 20)
#     draw_text("H A N G M A N", Point(10, 18), win)
#     draw_noose(win)
#     win.getMouse()
#
#
# def draw_text(text, point, win):
#     message = Text(point, text)
#     message.draw(win)
#     return message
#
#
# def draw_noose(win):
#     base = Line(Point(5, 8), Point(10, 8))
#     vert_pole = Line(Point(7.5, 8), Point(7.5, 15))
#     hor_pole = Line(Point(7.5, 15), Point(10.5, 15))
#     rope = Line(Point(10.5, 15), Point(10.5, 14))
#     base.draw(win)
#     vert_pole.draw(win)
#     hor_pole.draw(win)
#     rope.draw(win)


def main():
    # add other function calls here
    play()
    # graphics_display()
    pass


main()
