infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')
line = infile.readline().strip()
line_list = []
while line != '':
    line_list.append(line)
    line = infile.readline().strip()
for i in range(1, len(line_list)+1):
    outfile.write(f'{line_list[-i]}\n')
infile.close()
outfile.close()
