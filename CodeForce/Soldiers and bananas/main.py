x=input()
x=x.split(' ')
price=int(x[0])
dollars=int(x[1])
banana=int(x[2])
total=0
for i in range(1,banana+1):
    total=total+(i*price)
if total>dollars:
  dollars=total-dollars
  print(dollars)
else:
    print(0)
