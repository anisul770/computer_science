Rold=int(input('Type the initial value: '))
a=32310901
b=1729
m=224
for i in range(100):
    Rnew=(a*Rold+b)%m
    print(Rnew)
    Rold=Rnew
