def get_data(file):
    try:
        with open(file, 'r') as infile:
            line = infile.readline().strip()
            line = infile.readline().strip()
            bond_list = []
            while line != '':
                tmp_line = line.split('  ')
                bond_list.append(tmp_line)
                line = infile.readline().strip()
    except IOError:
        print("File dose not exist")
        exit()
    return bond_list


def input_check(data):
    bond_list = get_data('covalent.txt')
    for i in range(len(bond_list)):
        if data in bond_list[i]:
            index = bond_list[i].index(data)
            for j in range(len(bond_list[i])):
                if j == index:
                    continue
                else:
                    if j == 0:
                        print(bond_list[i][j], end=' ')
                    elif j == 1:
                        print(f'{bond_list[i][j]}KJ/mol', end=' ')
                    else:
                        print(f'{bond_list[i][j]}nm', end=' ')
            print()


def main():
    data = input('Enter any data: ').upper()
    input_check(data)


if __name__ == '__main__':
    main()
