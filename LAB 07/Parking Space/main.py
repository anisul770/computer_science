
def parking_space(n):
    space = ['_']*int(n)
    return space


def incoming_car(parking):
    done = False
    count = 1
    while not done:
        car = input("Another car ? (y/n)").strip().lower()
        if car == "n":
            done = True
        else:
            parking = filling_spaces(count, parking)
        count += 1
        for i in range(len(parking)):
            print(parking[i], end='')
        print()


def filling_spaces(car, parking):
    middle = len(parking)//2
    for i in range(int(car)):
        parking[middle] = 'X'
        middle = middle//2
    return parking


def main():
    n = input('Enter the number of parking space :').strip()
    parking = parking_space(n)
    for i in range(int(n)):
        print(parking[i], end='')
    print()
    incoming_car(parking)


if __name__ == '__main__':
    main()
