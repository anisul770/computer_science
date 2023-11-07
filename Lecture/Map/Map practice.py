def map_data(file):
    try:
        with open(file) as infile:
            line = infile.readline().strip()
            main_map = []
            while line != '':
                main_map.append(line)
                line = infile.readline().strip()
        return main_map
    except IOError:
        print(f'{file} does not exist')
        exit()


def coordinate_check(main_map, x, y):
    if y <= len(main_map) and x <= len(main_map[0]):
        if main_map[y][x] == '=':
            print('On the sea')
        if main_map[y][x] == '*':
            print('On the land')
            size = land_size(main_map, x, y)
            print(f'Size of the land {size[0]}x{size[1]}')
    else:
        print('Coordinate out of range')


def land_size(main_map, x, y):
    x_first_point = x
    x_count = 0
    y_first_point = y
    y_count = 0
    for i in range(y, 0, -1):
        if main_map[i][x] == '*':
            y_first_point = i
        elif main_map[i][x] == '=':
            break
    for i in range(x, 0, -1):
        if main_map[y][i] == '*':
            x_first_point = i
        elif main_map[y][i] == '=':
            break
    for i in range(x_first_point, len(main_map[y])):
        if main_map[y][i] == '*':
            x_count += 1
        elif main_map[y][i] == '=':
            break
    for i in range(y_first_point, len(main_map)):
        if main_map[i][x] == '*':
            y_count += 1
        elif main_map[i][x] == '=':
            break

    return x_count, y_count


def main():
    x = int(input('Enter x Coordinate: ').strip())
    y = int(input('Enter y Coordinate: ').strip())
    main_map = map_data('map.txt')
    coordinate_check(main_map, x, y)


if __name__ == '__main__':
    main()
