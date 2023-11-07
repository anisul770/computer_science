
try:
    area_file = open("country_area_km2.txt", "r")
    pop_file = open("country_pop.txt", "r")
    density_file = open("country_density.txt", "w")

except IOError as my_exception:
    print("ERROR: File not found")
    print(str(my_exception))
    exit()

line1 = area_file.readline()
line2 = pop_file.readline()

while line1 != "" and line2 != "":
    line_1 = line1.rsplit(maxsplit=1)
    line_2 = line2.rsplit(maxsplit=1)

    try:
        density = int(line_2[1])/int(line_1[1])
        density_file.write(f"{line_2[0]} \t{density:.2f}\n")
    except ValueError as my_exception:
        print("ERROR: wrong value", str(my_exception))
        #exit()
    line1 = area_file.readline()
    line2 = pop_file.readline()

area_file.close()
pop_file.close()
density_file.close()
