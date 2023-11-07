def instruction():
    infile = open('ApplePieRecipe.txt', "r")
    read_line = infile.readline().strip()
    done = False
    list = []
    while not done:
        if read_line == 'Instructions':
            done = True
        read_line = infile.readline().strip()
    while read_line != '':
        tmp_list = read_line.split()
        for i in range(len(tmp_list)):
            tmp_list[i] = tmp_list[i].strip('.,;')
            list.append(tmp_list[i])
        read_line = infile.readline()
    infile.close()
    return list


def find_word(instruction, key):
    key_list = []
    for i in range(len(key)):
        for j in instruction:
            if key[i] in j:
                key_list.append(j)
    return key_list


def main():
    infile = open('keyCode.txt', 'r')
    key = infile.readline().strip()
    list_of_possible_word = find_word(instruction(), key)
    for i in find_word(instruction(), key):
        for j in key:
            if j == i[0]:
                list_of_possible_word.remove(i)
    for i in list_of_possible_word:
        if len(i) <= 3:
            list_of_possible_word.remove(i)
    for i in list_of_possible_word:
        if len(i) <= 3:
            list_of_possible_word.remove(i)
    for j in key:
        for i in list_of_possible_word:
            if j in i:
                print(i[0], end='')


if __name__ == '__main__':
    main()
