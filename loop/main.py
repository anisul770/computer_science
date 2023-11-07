a=32310901
b=1729
m=224
rold = input("an initial value")
numbers = 0
while numbers<100:
    rnew= (a*int(rold)+b)%m
    print("numbers",rnew)
    numbers += 1
    rold=rnew
