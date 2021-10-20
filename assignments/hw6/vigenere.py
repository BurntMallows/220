"""
Name: <Queen Hamilton, II>
<vigenere>.py

Problem: This program encrypts an entered message using an entered key

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


from graphics import Text, GraphWin, Point, Entry, Rectangle


def code(message, keyword):
    message = message.replace(" ", "")
    message = message.upper()
    keyword = keyword.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    acc = ""
    for i in range(len(message)):
        num = ord(message[i]) - 65
        k = ord(keyword[i % len(keyword)]) - 65
        evaluate = (num + k) % 26
        letter = alphabet[evaluate]
        acc = acc + letter
    return acc


def screen_text(point, words, win):
    message_text = Text(point, words)
    message_text.draw(win)
    return message_text


def draw_entry(point, width, win):
    input_box = Entry(point, width)
    input_box.draw(win)
    return input_box


def main():
    win = GraphWin("Vigenere", 700, 500)
    win.setCoords(0, 0, 10, 10)

    screen_text(Point(2, 8), "Message to code", win)
    screen_text(Point(2, 7), "Enter Keyword", win)

    message_box = draw_entry(Point(6, 8), 40, win)
    key_box = draw_entry(Point(5, 7), 25, win)

    encode_button = Rectangle(Point(4, 4.5), Point(6, 5.5))
    encode_button.draw(win)
    encode_text = screen_text(Point(5, 5), "Encode", win)

    win.getMouse()
    encode_text.undraw()
    encode_button.undraw()
    message = message_box.getText()
    keyword = key_box.getText()

    cypher = code(message, keyword)
    screen_text(Point(5, 5.5), "Resulting Message", win)
    screen_text(Point(5, 5), cypher, win)

    screen_text(Point(5, 1), "Click anywhere to close the window", win)
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
