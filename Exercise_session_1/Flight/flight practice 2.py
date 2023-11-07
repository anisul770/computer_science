def get_data(file):
    try:
        with open(file, 'r') as infile:
            line = infile.readline().strip()
            flight_list = []
            while line != "":
                tmp = line.split(',')
                flight_list.append(tmp)
                line = infile.readline().strip()
            return flight_list
    except IOError:
        print(f'{file} dose not exist')
        exit()


def travel_time(arrival, departure):
    depart_min = int(departure.split(':')[1]) + int(departure.split(':')[0])*60
    arrival_min = int(arrival.split(':')[1]) + int(arrival.split(':')[0])*60
    total = (((arrival_min - depart_min)//60), ((arrival_min - depart_min) % 60))
    total_time = ((arrival_min - depart_min), total)
    return total_time


def direct_flight(flight_list, arrival, departure):
    print('Direct Flights are: ')
    option = 0
    for i in range(len(flight_list)):
        if flight_list[i][2] == departure and flight_list[i][4] == arrival:
            print(f'{flight_list[i][1]} {departure} --> {flight_list[i][3]} {arrival}')
            print(f'Total flight time {travel_time(flight_list[i][3], flight_list[i][1])[1][0]}:{travel_time(flight_list[i][3], flight_list[i][1])[1][1]}')
            option += 1
            print()
    if option == 0:
        print('No direct flight')


def change_flight(flight, arrival, departure):
    print('Changes flights are:')
    for i in range(len(flight)):
        for j in range(len(flight)):
            time = travel_time(flight[j][1], flight[i][3])[0]
            if flight[i][2] == departure and flight[j][4] == arrival and flight[i][4] == flight[j][2] and time >= 30:
                print(f'{flight[i][1]} {departure} --> {flight[i][3]} {flight[i][4]}')
                print(f'{flight[j][1]} {flight[j][2]} --> {flight[j][3]} {arrival}')
                print(f'Total flight time {travel_time(flight[j][3], flight[i][1])[1][0]}:{travel_time(flight[j][3], flight[i][1])[1][1]}')
                print()


def main():
    departure = input("Enter the departure city: ").strip().upper()
    arrival = input("Enter the arrival city: ").strip().upper()
    direct_flight(get_data('flights.txt'), arrival, departure)
    change_flight(get_data('flights.txt'), arrival, departure)


main()
