def get_data(file):
    try:
        with open(file, 'r') as infile:
            line = infile.readline().strip()
            player = []
            while line != '':
                tmp = line.split(';', 2)
                player.append(tmp)
                line = infile.readline().strip()
        return player
    except IOError:
        print(f"{file} doesn't exist")
        exit()


def top_player(file):
    player = get_data(file)
    result = []
    for i in range(len(player)):
        tmp = player[i][2].split(";")
        result.append(tmp)
        value = 0
        for j in range(len(result[i])):
            value = value + int(result[i][j])
        player[i][2] = value
    ranked_player = sorted(player, key=lambda x: -x[2])
    print(ranked_player)
    return ranked_player, result


def main():
    all_player = get_data('bowling.txt')
    player = top_player('bowling.txt')[0]
    for i in range(len(player)):
        for j in range(len(player[0])):
            print(player[i][j], end=' ')
        print()
    result = top_player('bowling.txt')[1]
    most = 0
    most_zero = 0
    zero_index = 0
    index = 0
    for i in range(len(result)):
        count = 0
        tmp = 0
        for j in range(len(result[i])):
            if result[i][j] == '10':
                tmp += 1
            if result[i][j] == '0':
                count += 1
        if i == 1:
            most_zero = count
        if count > most_zero:
            most_zero = count
            zero_index = i
        if i == 1:
            most = tmp
        if tmp > most:
            most = tmp
            index = i
    print(f'{all_player[index][0]} {all_player[index][1]} has knocked down all the pins {most} times')
    if most_zero != 0:
        print(f'{all_player[zero_index][0]} {all_player[zero_index][1]} has missed all the pins {most_zero} time (s)')


if __name__ == '__main__':
    main()
