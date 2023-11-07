def get_data(file):
    try:
        with open(file, 'r') as infile:
            line = infile.readline().strip()
            all_action = []
            while line != "":
                tmp = line.split(' ')
                all_action.append(tmp)
                line = infile.readline().strip()
        return all_action
    except Exception as problem:
        print(problem)
        exit()


def action_check(action):
    alice = set()
    count = 1
    for i in range(len(action)):
        if len(alice) <= 42:
            if action[i][0] == 'Bob':
                alice.add(action[i][3])
            if action[i][0] == 'Carl':
                if action[i][3] in alice:
                    alice.discard(action[i][3])
                else:
                    print(f'{count} Alice dose not have {action[i][3]}')
                    count += 1
        else:
            print('Alice space')


def main():
    file = ['actions', 'actions-fail_bob', 'actions-fail_carl']
    for i in file:
        action_check(get_data(f'{i}.txt'))


if __name__ == '__main__':
    main()
