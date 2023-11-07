def bond_list(file):
    try:
        with open(file, 'r') as infile:
            line = infile.readline().strip()
            line = infile.readline().strip()
            list_bond = []
            while line != '':
                line = line.split('  ')
                list_bond.append(line)
                line = infile.readline().strip()

    except IOError:
        print('File does not exist')

    return list_bond


def input_check(data):
    list_bond = bond_list('covalent.txt')
    for i in range(len(list_bond)):
        if data in list_bond[i]:
            for j in range(len(list_bond[i])):
                if data == list_bond[i][j]:
                    continue
                else:
                    if j == 1:
                        print(f'{list_bond[i][j]}KJ/mol', end=' ')
                    if j == 2:
                        print(f'{list_bond[i][j]}nm', end=' ')
                    if j == 0:
                        print(f'{list_bond[i][j]}', end=' ')
            print()


def main():
    data = input("Type any data: ").strip()
    input_check(data)


if __name__ == '__main__':
    main()
