
inFile = open("marys_lamp.txt", "r")
line = inFile.readline()
while line != "":
    # print(line.rstrip())
    words = line.split()
    for word in words:
        print(word.rstrip(".,'!;"))
    # print(line,end="")
    line = inFile.readline()

inFile.close()
