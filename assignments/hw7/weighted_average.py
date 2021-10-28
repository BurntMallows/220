"""
Name: <Queen Hamilton, II>
<weighted_average>.py

Problem: This program calculates the weighted average of a set of students

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def weight_calc(weight):
    acc = 0
    for i in range(len(weight)):
        acc = acc + int(weight[i])
    return acc


def average_calc(weight, grades):
    acc = 0
    for i in range(len(weight)):
        multiply = int(weight[i]) * int(grades[i])
        acc = acc + multiply
    average = acc / 100
    return average


def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    total = 0
    count = 0
    for line in infile:
        line = line.strip()
        name, scores = line.split(": ")
        scores = scores.split()
        weight = scores[::2]
        grades = scores[1::2]
        outfile.write(str(name) + "'s average: ")
        weight_total = weight_calc(weight)
        if weight_total == 100:
            average = average_calc(weight, grades)
            outfile.write(str(round(average, 1)) + "\n")
            total = total + average
            count = count + 1
        elif weight_total > 100:
            outfile.write("Error: The weights are more than 100." + "\n")
        else:
            outfile.write("Error: The weights are less than 100." + "\n")
    class_average = total / count
    outfile.write("Class average: " + str(round(class_average, 1)))

    infile.close()
    outfile.close()


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == "__main__":
    main()
