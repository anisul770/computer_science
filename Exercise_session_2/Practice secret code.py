def instruction(file):
    with open(file, "r") as infile:
        line = infile.readline().strip()
        list_word = []
        done = False
        while not done:
            if line == "Instructions":
                done = True
            line = infile.readline().strip()
        while line != '':
            tmp_list = line.strip().split(' ')
            for i in range(len(tmp_list)):
                list_word.append(tmp_list[i].strip('.,;'))
            line = infile.readline()
    return list_word


def find_word(list_word, file):
    with open(file, 'r') as infile:
        line = infile.readline().strip()
        key_word = []
        for i in range(len(line)):
            for j in list_word:
                if line[i] in j and len(j) > 3 and j[0] != line[i]:
                    key_word.append(j)
        return key_word


def main():
    key = find_word(instruction('ApplePieRecipe.txt'), 'keyCode.txt')
    print(key)
    for i in key:
        print(i[0], end='')


main()
