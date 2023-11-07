inFile = open("map.txt", "r")
main_map = []
line = inFile.readline()

while line != "":
    main_map.append(line.rstrip())
    line = inFile.readline()
for i in range(len(main_map)):
    for j in range(len(main_map[i])):
        print(main_map[i][j], end='')
    print()
ask_coordinates = True
while ask_coordinates:
    x = int(input("Please, enter the x : "))
    y = int(input("Please, enter the y : "))
    if x < 0 or y < 0:
        ask_coordinates = False
    if ask_coordinates:
        if x >= len(main_map[0]) or y >= len(main_map):
            print("coordinates out of range, please, try again!")
        else:
            if main_map[y][x] == "=":
                print("The coordinate is in the sea.")
            else:
                cnt_x = 0
                cnt_y = 0
                tmp_x = x
                tmp_y = y
                while main_map[tmp_y][tmp_x] == "*":
                    tmp_x = tmp_x - 1
                tmp_x = tmp_x + 1
                while main_map[tmp_y][tmp_x] == "*":
                    cnt_x = cnt_x + 1
                    tmp_x = tmp_x + 1
                tmp_x = tmp_x - 1
                while main_map[tmp_y][tmp_x] == "*":
                    tmp_y -= 1
                tmp_y += 1
                while main_map[tmp_y][tmp_x] == "*":
                    cnt_y = cnt_y + 1
                    tmp_y += 1
                print(f"the coordinates: {x}, {y} are in an island of size : {cnt_x}x{cnt_y} ")
inFile.close()

# x_y = input('Coordinate: ')
# map_list = []
# for i in range(len(map)):
#     list = [map[i]]
#     map_list.append(list)
# if map_list[int(x_y[0])][0][int(x_y[2])] == '*':
#    print('its on the land')
# else:
#    print('In the sea')
# print(map_list)
