def main():
    infile = open("original_cards.txt", "r")
    set_of_cards = set()
    line = infile.readline()

    while line != "":
        set_of_cards.add(line.strip())
        line = infile.readline()
    # print(len(set_of_cards), set_of_cards)
    team = input("please, write the team name: ").upper()
    counter = 0
    for element in set_of_cards:
        if team in element.upper():
            counter += 1
            print(element[:len(element)-len(team)-9])
    print(f"The number of player in {team} is {counter}")


main()
