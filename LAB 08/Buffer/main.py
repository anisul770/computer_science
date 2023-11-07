number_string = input("Enter the sequence: ")
number_string = number_string.strip()
number_string = number_string.split(" ")
done = False
while not done:
    change = input('Do you want to change? (y/n) ').strip().lower()
    if change == "y":
        number_string.insert(0, number_string[-1])
        number_string.pop(-1)
        for i in number_string:
            print(i, end=' ')
        print()
    else:
        done = True
for i in number_string:
    print(i, end=' ')
