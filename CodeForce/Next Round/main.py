x=input()
y=input()
x=x.split(' ')
y=y.split(' ')
a=int(x[0])
b=0
for i in range(a):
      if int(y[(int(x[1])-1)])<=int(y[i]) and int(y[i])>0:
          b=b+1
print(b)
