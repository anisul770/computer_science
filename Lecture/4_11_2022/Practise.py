def integer(message):
    done = False
    while not done:
        value = input(message).strip()
        if value[0] == '-' and value[1:].isdigit() or value.isdigit():
            value = int(value)
            done = True
    return value


def max_avg(number):
    acc = 0
    for i in range(number):
        value = integer('Please, enter a number: ')
        if i == 0:
            max = value
        else:
            if max < value:
                max = value
        acc += value
    avg = acc/number
    return (avg, max)


def cube_volume(length):
    volume = length**3
    return volume


def square(size, character):
    for i in range(size):
        for j in range(size):
            print(character, end='')
        print()


def main():
    length = integer('Enter the length of the cube: ')
    print(f'The volume of the cube is {cube_volume(length)}')
    size = integer("Enter the square size: ")
    character = input("Enter the element: ")
    square(size, character)
    (avg, max) = max_avg(5)
    print(f'The average value is {avg} and max value among them is {max}')

if __name__ == '__main__':
    main()
