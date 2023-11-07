infile = open("..\\18_11_2022\\data.txt", "r")
outfile = open("output.dat", "w")
title = infile.readline()
line = infile.readline()
# 123
# "123\n"

acc = 0
i = 2
while line != "":
    value = int(line)
    acc = acc+value
    outfile.write(f"{value:^10}\n")
    print("- ",value)
    # print(f'{value:^{i}}')
    line = infile.readline()
    i = i + 3

outfile.write(f"Accumulator:{acc}\n")
print("= ",acc)
# print(f"Accumulator:{acc}\n")
infile.close()
outfile.close()
