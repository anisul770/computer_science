import random

number = int(input('Enter a integer number: '))
number_list = []
for i in range(number):
    number_list.append(random.randint(1, 6))
index_list = []
index = []
# max_num = 0
# max_count = 0
for i in range(len(number_list)-1):
    if number_list[i] == number_list[i+1]:
        j = i
        while number_list[i] == number_list[j]:
            # max_count += 1
            if i != j:
                index = [i, j]
            if j <= len(number_list)-1:
                j += 1
            if j == len(number_list):
                break
        index_list.append(index)
'''
        if max_num < max_count:
            max_num = max_count
        max_count = 0
'''
if len(index_list) != 0:
    maximum = index_list[0][1]-index_list[0][0] + 1
    index_num = 0
    for i in range(len(index_list)):
        if index_list[i][1]-index_list[i][0]+1 > maximum:
            maximum = index_list[i][1]-index_list[i][0] + 1
            index_num = i
    start = index_list[index_num][0]
    last = index_list[index_num][1]+1
    # print(index_list)
    # print(f'{number_list[:start]}({number_list[start:last]}){number_list[last:]}')
    for i in range(len(number_list)):
        if start == i:
            print('(', end=' ')
        if last == i:
            print(')', end=' ')
        print(number_list[i], end=' ')
else:
    print("No maximum sequence")
'''
def random_list(number):
    random_ = list()
    for i in range(number):
        tmp = random.randint(1, 6)
        random_.append(tmp)
    return random_


def index_max_same(number):
    number_list = random_list(number)
    index_list = []
    index = []
    for i in range(len(number_list)-1):
        if number_list[i] == number_list[i+1]:
            j = i
            while number_list[i] == number_list[j]:
                # max_count += 1
                if i != j:
                    index = [i, j]
                j += 1
            index_list.append(index)
    return index_list
    
        if max_num < max_count:
            max_num = max_count
        max_count = 0


def main():
    number = int(input('Enter a integer number: '))
    number_list = random_list(number)
    index_list = index_max_same(number)
    maximum = index_list[0][1]-index_list[0][0] + 1
    index_num = 0
    for i in range(len(index_list)):
        if index_list[i][1]-index_list[i][0] > maximum:
            maximum = index_list[i][1]-index_list[i][0] + 1
            index_num = i
    start = index_list[index_num][0]
    last = index_list[index_num][1]+1
    for i in range(len(number_list)):
        if start == i:
            print('(', end=' ')
        if last == i:
            print(')', end=' ')
        print(number_list[i], end=' ')
    print()
    print(number_list)


if __name__ == '__main__':
    main()
'''
