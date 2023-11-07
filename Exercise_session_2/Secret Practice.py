def data(file):
    try:
        with open(file, 'r') as infile:
            line = infile.readline().strip()
            list_word = []
            done = False
            while not done:
                if line == 'Instructions':
                    done = True
                line = infile.readline().strip()
            while line != '':
                line = line.strip()
                tmp_list = line.split(' ')
                for i in tmp_list:
                    list_word.append(i.strip('.,;-'))
                line = infile.readline()
        return list_word
    except IOError:
        print(f'{file} does not exist')
        exit()


def find_word(file):
    try:
        with open(file, 'r') as infile:
            line = infile.readline().strip()
            all_word = data('ApplePieRecipe.txt')
            word = []
            for i in line:
                for j in all_word:
                    if len(j) > 3 and j[0] != i and i in j:
                        word.append(j)
        return word
    except IOError:
        print(f'{file} does not exist')
        exit()


def main():
    key = find_word('keyCode.txt')
    for i in key:
        print(i[0], end='')


if __name__ == '__main__':
    main()
