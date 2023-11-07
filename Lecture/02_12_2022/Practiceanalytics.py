def main():
    infile = open('analiytics.txt', 'r')
    my_glossary = {}
    line = infile.readline().strip()
    while line != "":
        list_line = line.split(':')
        my_set = set()
        if list_line[1] in my_glossary:
            my_glossary[list_line[1]].add(int(list_line[0]))
        else:
            my_set.add(int(list_line[0]))
            my_glossary[list_line[1]] = my_set
        line = infile.readline().strip()
    print(my_glossary)
    for x, y in sorted(my_glossary.items()):
        print(f'{x}: ', end='')
        i = 0
        for element in sorted(y):
            if i < len(y) - 1:
                print(element, end=',')
            else:
                print(element)
            i += 1


if __name__ == '__main__':
    main()
