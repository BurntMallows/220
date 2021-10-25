"""
Name: <Queen Hamilton, II>
<lab8>.py
"""
from encryption import encode, encode_better


def main():
    # add other function calls here
    number_words("Walrus.txt", "Walrus_output.txt")
    hourly_wages("hourly_wages.txt", "hourly_wages_output.txt")
    check_sum = calc_check_sum("0072946520")
    print(check_sum)
    send_message("message.txt", "bob")
    key = int(input("Enter an integer key value: "))
    send_safe_message("secret_message.txt", "bobert", key)
    send_uncrackable_message("safest_message.txt", "bobbery", "pad.txt")


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    i = 1
    for line in infile:
        words = line.split()
        for words in words:
            outfile.write(str(i) + " " + words + "\n")
            i += 1

    infile.close()
    outfile.close()


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    for line in infile:
        split = line.split()
        wage = float(split[2])
        wage += 1.65
        wage = wage * int(split[3])
        outfile.write(split[0] + " " + split[1] + " " + str(wage) + "\n")

    infile.close()
    outfile.close()


def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc += int(isbn[i]) * pos
    return acc


def send_message(file, friend):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "wt")
    for line in infile:
        outfile.write(line)

    infile.close()
    outfile.close()


def send_safe_message(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "wt")
    for line in infile:
        x = encode(line, key)
        outfile.write(x)

    infile.close()
    outfile.close()


def send_uncrackable_message(file, friend, pad):
    infile = open(file, "r")
    pad_file = open(pad, "r")
    outfile = open(friend + ".txt", "wt")
    key = pad_file.read()
    for line in infile:
        x = encode_better(line, key)
        outfile.write(x)

    infile.close()
    outfile.close()


main()
