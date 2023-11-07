def get_data(file):
    try:
        with open(file, 'r') as infile:
            line = infile.readline().strip()
            player_set = set()
            while line != '':
                player_set.add(line)
                line = infile.readline().strip()
            player_list = list(player_set)
        return player_list
    except Exception as problem:
        print(problem)
        exit()


def player(player_list, name):
    for i in player_list:
        if name.upper() in i.upper():
            for j in range(len(i)):
                if i[j].isdigit():
                    index = j
                    break
            print(f'{i[0:index]}')


def main():
    name = input('Enter the team name: ').strip()
    player(get_data('original_card.txt'), name)


if __name__ == '__main__':
    main()
