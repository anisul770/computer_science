
def get_data(file_name):
    with open(file_name, 'r') as flights:
        flights_list = []
        line = flights.readline().strip()
        while line != '':
            line_list = line.split(',')
            flights_list.append(line_list)
            line = flights.readline().strip()
    return flights_list


def direct_flight(departure_city, arriving_city, flight_list):

    possible_direct_flight = []
    for r in range(len(flight_list)):
        if flight_list[r][2] == departure_city:
            if flight_list[r][4] == arriving_city:
                possible_direct_flight.append(flight_list[r])
    if possible_direct_flight:
        print("Possible direct flights are: ")
        for r in range(len(possible_direct_flight)):
            print(f"Option {r+1}")
            for c in range(len(possible_direct_flight[r])):
                if c != 2:
                    print(possible_direct_flight[r][c], end=' ')
                if c == 2:
                    print(possible_direct_flight[r][c], end=' -> ')
            print()
            travelling_time = traveling_time_minute(possible_direct_flight[r][3]) - traveling_time_minute(possible_direct_flight[r][1])
            print(f'Travelling time: {travelling_time_hour(travelling_time)}')

    else:
        print("There aren't possible direct flights")


def traveling_time_minute(time):

    time1 = time.split(':')
    minute_time = int(time1[0])*60 + int(time1[1])
    return minute_time


def travelling_time_hour(minute_time):
    hours = minute_time//60
    minute = minute_time % 60
    time_string = str(hours) + ":" + str(minute)
    return time_string


def change_flights(departing_city, arriving_city, flights_list):
    k = 1
    print("Possible change flights are: ")
    for r in range(len(flights_list)):
        if flights_list[r][2] == departing_city and flights_list[r][4] != arriving_city:
            for i in range(len(flights_list)):
                if flights_list[i][2] == flights_list[r][4] and flights_list[i][4] == arriving_city:
                    # print(flights_list[r],flights_list[i])
                    transit_time = traveling_time_minute(flights_list[i][1]) - traveling_time_minute(flights_list[r][3])
                    if transit_time >= 30:
                        print(f'Option {k}')
                        for j in range(len(flights_list[0])):
                            if j != 2:
                                print(flights_list[r][j], end=" ")
                            if j == 2:
                                print(flights_list[r][j], end=" -> ")
                        print()
                        for l in range(len(flights_list[0])):
                            if l != 2:
                                print(flights_list[i][l], end=" ")
                            if l == 2:
                                print(flights_list[i][l], end=" -> ")
                        print()
                        travelling_time = traveling_time_minute(flights_list[i][3]) - traveling_time_minute(flights_list[r][1])
                        print(f'Travelling time: {travelling_time_hour(travelling_time)} \n')
                    k += 1


def main():
    flights_list = get_data('flights.txt')
    departure_city = input("From what city do you want to depart? ").strip().upper()
    arriving_city = input("Where do you want to go?").strip().upper()
    direct_flight(departure_city, arriving_city, flights_list)
    print()
    change_flights(departure_city, arriving_city, flights_list)


if __name__ == '__main__':
    main()
