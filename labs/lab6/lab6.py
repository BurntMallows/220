"""
Name: <Queen Hamilton, II>
<lab6>.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Enter a first and last name: ")
    first_name, last_name = name.split(" ")
    print(last_name + ",", first_name)


def company_name():
    domain_name = input("Enter a 3-part domain name: ")
    domain_list = domain_name.split(".")
    print(domain_list[1])


def initials():
    name = int(input("How many names will be entered? "))
    for i in range(name):
        student_first = input("Enter the first name of student " + str(i + 1) + ": ")
        student_last = input("Enter " + student_first + "'s last name: ")
        student_in = student_first[0] + student_last[0]
        print(student_first + "'s initials are", student_in)


def names():
    names_list = input("Enter a list of names, separated by a comma: ")
    names_split = names_list.split(",")
    initial = ""
    for i in range(names_list.count(",") + 1):
        first_name, last_name = names_split[i].split()
        initial = initial + " " + first_name[0] + last_name[0]
    print("The initials are" + initial)


def thirds():
    sentences = int(input("How many sentences will be input: "))
    for i in range(sentences):
        sentence_string = input("Enter sentence " + str(i + 1) + ": ")
        sentence_int = sentence_string.count("")
        print(sentence_string[2:sentence_int:3])


def word_average():
    # instructor said it didn't need to loop
    sentence = input("Enter a sentence: ")
    sentence_split = sentence.split(" ")
    word_amount = sentence.count(" ") + 1
    acc = 0
    for i in range(word_amount):
        letter_count = sentence_split[i].count("") - 1
        acc = acc + letter_count
    average = acc / word_amount
    print(average)


def pig_latin():
    sentence = input("Enter a sentence: ")
    sentence_split = sentence.split(" ")
    latin = ""
    for i in range(sentence.count(" ") + 1):
        word = sentence_split[i].lower()
        latin = latin + " " + word[1:] + word[0] + "ay"
    print(sentence + " ->" + latin)


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()
    # add other function calls here


main()
