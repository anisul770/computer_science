def main():

    list1 = [1, 4, 9, 16, 9, 11, 4]
    list2 = [11, 9, 7, 16, 9, 11, 4, 4, 1]
    print(same_set(list1, list2))


def same_set(a, b):
    a = set(a)
    b = set(b)
    if a == b:
        x = 'Yes'
    else:
        x = 'No'

    return x


if __name__ == '__main__':
    main()
