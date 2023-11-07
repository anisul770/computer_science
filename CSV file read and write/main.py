import csv

f = open('test_file.txt', 'w')
f.write('test text')
f.close()

g = open('people.csv', 'a', newline='')
tup1 = ('bob', 19)
writer = csv.writer(g)
writer.writerow(tup1)
g.close()
