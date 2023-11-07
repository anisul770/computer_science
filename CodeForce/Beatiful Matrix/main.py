y=0
z=0
for i in range(1,6):
    x=input()
    x=x.split()
    for j in range(1,6):
        if int(x[j-1])==1:
            y=j
            z=i
a=0
b=0
while y>z or y<z or (x!=3 and y!=3):
   if y>3 or y<3:
    if y>3:
        y=y-1
    if y<3:
        y=y+1
    a=a+1
   if z<3 or z>3:
       if z<3:
           z=z+1
       if z>3:
           z=z-1
       b=b+1
print(a+b)
