"""
Name: <Queen Hamilton, II>
<lab13>.py
"""


from graphics import Rectangle, Point


def is_in_binary(search_val, values):
    mid = len(values) // 2
    while values[mid] != search_val and len(values) != 1:
        if values[mid] > search_val:
            values = values[:mid]
        else:
            values = values[mid:]
        mid = len(values) // 2
    if len(values) == 1 and values[0] != search_val:
        return False
    else:
        return True


def selection_sort(values):
    for i in range(0, len(values)):
        lowest = values[i]
        position = i
        for j in range(i + 1, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                position = j
        values[i], values[position] = values[position], values[i]
    print(values)


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return dx * dy


def rect_sort(rectangles):
    dictionary = {}
    areas = []
    for rect in rectangles:
        dictionary[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(0, len(areas)):
        rectangles[i] = dictionary[areas[i]]
    print(rectangles)


def star_find(filename):
    file = open(filename, "r")
    signals = file.read().split()
    found = []
    for i in signals:
        if 4000 <= int(i) <= 5000:
            found.append(i)
        if len(found) == 5:
            last = i
            break
    if len(found) < 5:
        print("5 signals could not be found")
    print("{0} signals were found.".format(len(found)))
    print("The signals' strengths are: {0}".format(found))
    print("The fifth signal was found after {0} searches".format(last))


def main():
    # add other function calls here
    print(is_in_binary(3, [1, 2, 3, 4, 6, 7, 8]))
    print(is_in_binary(5, [1, 2, 3, 4, 6, 7, 8]))
    selection_sort([2, 7, 98, 4, 2045, 0, 123, 6, 14, 73, 40, 12])
    rect1 = Rectangle(Point(0, 0), Point(5, 5))
    rect2 = Rectangle(Point(0, 0), Point(7, 8))
    rect3 = Rectangle(Point(0, 0), Point(10, 14))
    rectangles = [rect2, rect3, rect1]
    rect_sort(rectangles)
    star_find("signals.txt")
    pass


main()
