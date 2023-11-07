j=int(input())
for i in range(j):
    x=input()
    y=len(x)
    z=x[1:y-1]
    if y<=10:
     print(x)
    else:
     print(x[0],end='')
     print(len(x[1:-1]),end='')
     print(x[len(x)-1])
