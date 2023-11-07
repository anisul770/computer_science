with open("data.txt", "r") as infile:
    line = infile.readline()
    while line != "":
        value = int(line)
        value = value * 10
        try:
            if value > 500 :
             raise ValueError("Amount is higher than the reference " + str(value))
            print(value)
            line = infile.readline()
        except ValueError as my_exception:
            print("ERROR", str(my_exception))
            exit()
