x=int(input())
y=str(x)
z=0
for i in range(len(y)):
    if x%10==4 or x%10==7:
      z=z+1
    x=x//10
if z==len(y) and z!=1:
    print('YES')
else:
    print('NO')
