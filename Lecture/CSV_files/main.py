import csv

from csv import reader
from csv import writer

infile = open('csv_films_file.csv', 'r')
csvReader = reader(infile)
outfile = open("output_csv_file.csv", "w", newline='')
csvWriter = writer(outfile)

for row in csvReader:
    print(row)
    csvWriter.writerow(row)


infile.close()
outfile.close()
