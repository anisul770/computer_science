import csv

from csv import reader
from csv import writer

infile = open('original_cards.txt', 'r')
outfile = open('cards_players.csv', "w", newline='')

csvWriter = writer(outfile)

players_set = set()

line = infile.readline()

while line != "":
    line = line.strip()
    players_set.add(line)
    line = infile.readline()

for player in players_set:
    first_digit = 0
    last_digit = 0
    player_list = []
    for i in range(len(player)):
        if player[i].isdigit():
            if first_digit == 0:
                first_digit = i
            else:
                last_digit = i
    player_list.append(player[:first_digit-1])
    player_list.append(player[first_digit:last_digit+1])
    player_list.append(player[last_digit+2:])
    print(player_list)
    csvWriter.writerow(player_list)

infile.close()
outfile.close()





