x=input()
x=x.split('+')
x=sorted(x)
for i in range(len(x)):
    print(x[i],end='')
    if i <len(x)-1:
     print('+',end='')
