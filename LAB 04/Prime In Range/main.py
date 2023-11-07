Number=int(input('Enter a number: '))
print('Prime Numbers from 1 to ',Number)
if Number==1:
    print(Number)
else:
 print(1)
 print(2)
 S=3
 j=3
 while j<=Number:
  x=False
  for i in range(2,j-1):
    if j%i==0:
      x=True
    S=S+1
  if x==False:
     print(j)
  j=j+1
