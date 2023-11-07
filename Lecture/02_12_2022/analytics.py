#
import random


def main():
    infile = open("analiytics.txt", "r")
    my_glosary = {}
    line = infile.readline()

    while line != "":
        line = line.strip()
        list_line = line.split(":")
        my_set = set()
        if list_line[1] in my_glosary:
            my_glosary[list_line[1]].add(int(list_line[0]))
        else:
            my_set.add(int(list_line[0]))
            my_glosary[list_line[1]] = my_set
        line = infile.readline()

    print(my_glosary)
    for item in sorted(my_glosary):
        print(item, end=": ")
        j = 0
        for element in sorted(my_glosary[item]):
            if j < len(my_glosary[item])-1:
                print(element,end=', ')
            else:
                print(element)
            j += 1

    infile.close()


main()
