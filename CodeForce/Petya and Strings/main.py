x=input()
y=input()
x=x.lower()
y=y.lower()
i=0
if x==y:
    print(0)
else:
 while ord(x[i])==ord(y[i]):
   i=i+1
 X=ord(x[i])
 Y=ord(y[i])

 if X>Y:
    print(1)
 else:
    print(-1)

