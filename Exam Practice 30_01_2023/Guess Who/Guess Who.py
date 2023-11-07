def get_data(file):
    try:
        with open(file, 'r') as infile:
            line = infile.readline().strip()
            all_char = []
            while line != '':
                tmp = line.split(';')
                all_char.append(tmp)
                line = infile.readline().strip()
        return all_char
    except IOError:
        print(f'{file} does not exist')
        exit()


def guess(all_char, file):
    try:
        with open(file, 'r') as infile:
            line = infile.readline().strip()
            step = 1
            win_list = []
            selected = []
            while line != "":
                line = line.split(' = ')
                print(f'Step {step} - question: {line[0]} = {line[1]}')
                print('Selected Characters:')
                for k in range(len(all_char[0])):
                    if line[0] == all_char[0][k]:
                        for i in range(len(all_char)):
                            if line[1] == all_char[i][k]:
                                if step == 1:
                                    selected.append(all_char[i])
                                if all_char[i] in selected:
                                    if step == 3:
                                        win_list.append(all_char[i])
                                    print(all_char[i][0], end=' - ')
                                    for j in range(1, len(all_char[i])):
                                        print(f'{all_char[0][j]}: {all_char[i][j]}', end=', ')
                                    print()
                line = infile.readline().strip()
                print()
                step += 1
            if len(win_list) != 1:
                print('Too bad, you lose.')
            elif len(win_list) == 1:
                print(f'Congratulation, you win! Character selected: ')
                print(win_list[0][0], end=' - ')
                for j in range(1, len(all_char[i])):
                    print(f'{all_char[0][j]}: {win_list[0][j]}', end=', ')
                print()
    except IOError:
        print(f'{file} does not exist')
        exit()


def main():
    guess(get_data('characters.txt'), 'question1.txt')


if __name__ == '__main__':
    main()
