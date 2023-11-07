
def get_data(file):
    with open(file, 'r') as infile:
        line = infile.readline().strip()
        flight_list = []
        while line != '':
            tmp_list = line.split(',')
            flight_list.append(tmp_list)
            line = infile.readline().strip()
    return flight_list


def direct_flight(departure, arrival, flight_list):
    print('Direct flights are: ')
    direct = False
    k = 1
    for i in range(len(flight_list)):
        if flight_list[i][2] == departure and flight_list[i][4] == arrival:
            print(f'Option {k}')
            print(f'{flight_list[i][0]} {flight_list[i][1]} {flight_list[i][2]} -> {flight_list[i][3]} {flight_list[i][4]} {flight_list[i][5]}')
            print(f'Total time: {time_string(travelling_time(flight_list[i][1], flight_list[i][3]))}')
            k += 1
            direct = True
    if not direct:
        print("No direct flights")


def travelling_time(time1, time2):
    tmp_min2 = time2.split(':')
    arrival_minute = int(tmp_min2[0])*60 + int(tmp_min2[1])
    tmp_min1 = time1.split(':')
    departure_minute = int(tmp_min1[0])*60 + int(tmp_min1[1])
    total_time = arrival_minute - departure_minute
    return total_time


def time_string(time):
    total_time_hour = time//60
    total_time_min = time % 60
    time_str = str(total_time_hour) + ':' + str(total_time_min)
    return time_str


def change_flights(departure, arrival, flight_list):
    print("Change flights are: ")
    change = False
    k = 1
    for i in range(len(flight_list)):
        if flight_list[i][2] == departure and flight_list[i][4] != arrival:
            for j in range(len(flight_list)):
                if flight_list[j][2] == flight_list[i][4] and flight_list[j][4] == arrival:
                    time = travelling_time(flight_list[i][3], flight_list[j][1])
                    if time >= 30:
                        print(f'Option {k}')
                        print(f'{flight_list[i][0]} {flight_list[i][1]} {flight_list[i][2]} -> {flight_list[i][3]} {flight_list[i][4]} {flight_list[i][5]}')
                        print(f'{flight_list[j][0]} {flight_list[j][1]} {flight_list[j][2]} -> {flight_list[j][3]} {flight_list[j][4]} {flight_list[j][5]}')
                        print(f'Total time {time_string(travelling_time(flight_list[i][1], flight_list[j][3]))}')
                        print()
                        k += 1
                        change = True
    if not change:
        print("No Change Flight")


def main():
    departure = input("Enter departure city: ").upper().strip()
    arrival = input("Enter arrival city: ").strip().upper()
    flight_list = get_data('flights.txt')
    direct_flight(departure, arrival, flight_list)
    print()
    change_flights(departure, arrival, flight_list)


if __name__ == '__main__':
    main()
