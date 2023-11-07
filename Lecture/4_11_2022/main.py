def main():
   size = int(input('Enter the length: '))
   character = input('Enter the element: ')
   print_square(size, character)
   value=get_integer('Enter,the size of the cube')
   print(f'The volume of the cube is {cube_volume(value)}')
   (AVG, MAX) = max_avg(5)
   print(MAX, AVG)


def cube_volume(sidelength):
    volume = sidelength**3
    return volume


def print_square(size, character):
    for i in range(size):
        for j in range(size):
            print(character, end='')
        print()


def get_integer(message):
    done = False
    while not done:
        value = input(message).strip()
        if value[0] == '-' and value[1:].isdigit() or value.isdigit():
            int_value = int(value)
            done = True
    return int_value


def max_avg(number):
    acc = 0
    for i in range(number):
        value = get_integer('Please,enter an integer: ')
        if i == 0:
            max = value
        else:
            if max < value:
                max = value
        acc = acc+value
    avg = acc/number
    return (avg, max)


main()
