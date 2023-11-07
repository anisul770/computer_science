
seat_list = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
             [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
             [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
             [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
             [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
             [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
             [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
             [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
             [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]]
price_set = set()
for i in range(len(seat_list)):
    for j in range(len(seat_list[i])):
        price_set.add(seat_list[i][j])
price_set = sorted(price_set)


def seat_number(_list, seatlist):
    customer = input('Type seat or price?').strip().lower()
    if customer.startswith('s'):
        seat = input('specify a seat row and column: ').strip()
        seat_index = seat.split(' ')
        if seatlist[int(seat_index[0])][int(seat_index[1])] != 0:
            print(f'Selected seat price {seatlist[int(seat_index[0])][int(seat_index[1])]}')
            yn = input('Do you want to buy it? (y/n) ').strip().lower()
            if yn.startswith('y'):
                seatlist[int(seat_index[0])][int(seat_index[1])] = 0
                print('Thanks')
        else:
            print('This seat is sold')
    else:
        print('Chose a price \n', _list)
        price = int(input())
        print(f'Available seats are')
        for k in range(len(seatlist)):
            for l in range(len(seatlist[k])):
                if seatlist[k][l] == price and seatlist[k][l] != 0:
                    print(f'row {k} column {l}', end=' ')
        print()
        seat = input('Chose a seat row and column: ').strip()
        seat_index = seat.split(' ')
        seatlist[int(seat_index[0])][int(seat_index[1])] = 0
        print('Thanks')


def main():
    yn = input('Do you want to buy a Ticket? (y/n) ').strip().lower()
    while not yn.startswith('n'):
        seat_number(price_set, seat_list)
        yn = input('Do you want to buy a Ticket? (y/n) ').strip().lower()
    for a in range(len(seat_list)):
        for b in range(len(seat_list[a])):
            print(seat_list[a][b], end=' ')
        print()


if __name__ == '__main__':
    main()
