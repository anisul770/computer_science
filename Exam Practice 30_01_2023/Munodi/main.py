def get_data(file):
    try:
        with open(file) as infile:
            line = infile.readline().strip()
            number_list = []
            while line != "":
                tmp = line.split(' ')
                number_list.append(tmp)
                line = infile.readline().strip()
        return number_list
    except IOError:
        print(f'{file} does not exist')
        exit()


def sequence_check(number_list):
    for i in range(len(number_list)):
        for j in range(len(number_list[i])):
            if j < len(number_list):
                if int(number_list[i][j]) % 2 == 0 and int(number_list[i][j])/2 == int(number_list[i][j+1]):
                    continue
                if int(number_list[i][j]) % 2 != 0 and int(number_list[i][j+1]) == 3*int(number_list[i][j]) + 1:
                    continue
                else:
                    print('Not mundi')


def main():
    number_list = get_data('seq.txt')
    sequence_check(number_list)


if __name__ == '__main__':
    main()
