y=int(input())
x=0
for i in range(y):
    z=input()
    z=z.upper()
    if z=='X++' or z=='++X':
        x=x+1
    if z=='X--' or z=='--X':
        x=x-1
print(x)
