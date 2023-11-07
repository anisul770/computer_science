def all_player(file):
    try:
        with open(file) as infile:
            line = infile.readline().strip()
            player_dict = {}
            while line != "":
                tmp = line.split(',')
                if tmp[2].strip() in player_dict:
                    player_dict[tmp[2].strip()].append([tmp[0].strip(), tmp[3].strip()])
                elif tmp[2].strip() not in player_dict:
                    temp = [tmp[0].strip(), tmp[3].strip()]
                    player_dict[tmp[2].strip()] = [temp]
                line = infile.readline().strip()
        return player_dict
    except IOError:
        print(f'{file} dose not exist')
        exit()


def selection(player_dict):
    goalkeeper = []
    midfielder = []
    forward = []
    defender = []
    mid_budget = 80
    defender_budget = 40
    keeper_budget = 20
    forward_budget = 120
    for i in range(len(player_dict['goalkeeper'])):
        if int(player_dict['goalkeeper'][i][1]) <= keeper_budget and len(goalkeeper) < 3:
            goalkeeper.append(player_dict['goalkeeper'][i])
            keeper_budget -= int(player_dict['goalkeeper'][i][1])
    mid_budget += keeper_budget
    for i in range(len(player_dict['midfielder'])):
        if int(player_dict['midfielder'][i][1]) <= mid_budget and len(midfielder) < 8:
            midfielder.append(player_dict['midfielder'][i])
            mid_budget -= int(player_dict['midfielder'][i][1])
    forward_budget += mid_budget
    for i in range(len(player_dict['forward'])):
        if int(player_dict['forward'][i][1]) <= forward_budget and len(forward) < 6:
            forward.append(player_dict['forward'][i])
            forward_budget -= int(player_dict['forward'][i][1])
    defender_budget += forward_budget
    for i in range(len(player_dict['defender'])):
        if int(player_dict['defender'][i][1]) <= defender_budget and len(defender) < 8:
            defender.append(player_dict['defender'][i])
            defender_budget -= int(player_dict['defender'][i][1])
    return goalkeeper, defender, midfielder, forward


def main():
    player_dict = all_player('fantafoot.txt')
    (Goalkeeper, Defender, Midfielder, forward) = selection(player_dict)
    print("Goalkeeper", end=': ')
    for i in range(len(Goalkeeper)):
        print(Goalkeeper[i][0], ' ', Goalkeeper[i][1], end=' ')
    print()
    print('Defender', end=': ')
    for i in range(len(Defender)):
        print(Defender[i][0], ' ', Defender[i][1], end=' ')
    print()
    print('Midfielder', end=': ')
    for i in range(len(Midfielder)):
        print(Midfielder[i][0], ' ', Midfielder[i][1], end=' ')
    print()
    print('Forward', end=': ')
    for i in range(len(forward)):
        print(forward[i][0], ' ', forward[i][1], end=' ')


if __name__ == '__main__':
    main()
