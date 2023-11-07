infile = open('enola.txt', 'r')
outfile = open('output.txt', 'w')
line_in = infile.readline().strip()
n = 1
while line_in != '':
    outfile.write(f'/*{n}*/{line_in}\n')
    line_in = infile.readline().strip()
    n += 1


infile.close()
outfile.close()
