x=int(input())
a=0
for i in range(x):
 z=0
 y=input()
 if y[0]=='1':
    z=z+1
 if y[2]=='1':
    z=z+1
 if y[4]=='1':
    z=z+1
 if z==2 or z==3:
    a=a+1
print(a)
