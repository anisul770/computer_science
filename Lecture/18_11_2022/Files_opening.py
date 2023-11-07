#files
infile= open("data.txt","r")
second_file=open("..\\input.txt","r")
different_folder_file=open("C:\\Users\\Enamul Haque\\PycharmProjects\\Lecture\\28_10_2022\\Table.txt","w")

title=infile.readline()
line=title
while(line!=''):
 print(line,end='')
 line=infile.readline()
for line in second_file:
    print(line,end='')


infile.close()
second_file.close()
different_folder_file.close()
