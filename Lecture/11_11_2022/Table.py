import random

COUNTRIES = 8
MEDALS =3
counts=[[0,3,0],[0,0,1],[0,0,1],[1,0,0],[0,0,1],[3,1,1],[0,1,0],[1,0,1]]
ROWS=5
COLUMNS=20
new_table=[]
for i in range(ROWS):
    tmp_table=[]
    for j in range(COLUMNS):
        tmp_table.append(0)
    new_table.append(tmp_table)
print(new_table)
table=[]
COUNTRIES_name=['usa','it','arg','cad','uk','uae','bd','ind']
for i in range(ROWS):
    row=[0]*COLUMNS
    table.append(row)
for i in range(COUNTRIES):
    print('%8s'%COUNTRIES_name[i],end='')
    for j in range(MEDALS):
        print('%8d'%counts[i][j],end='')
    print()
print('Number of rows:',len(counts))
print('Number of columns:',len(counts[0]))
for i in range(ROWS):
    for j in range(COLUMNS):
        print(table[i][j],end=' ')
    print()
