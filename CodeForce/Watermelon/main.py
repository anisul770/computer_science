weight=int(input('How much is the weight?'))
Set=set()
x='NO'
for i in range(weight):
    if i%2==0 and i<weight-1:
     Set.add(i+2)
for i in Set:
    for j in Set:
        if i+j==weight:
            x='YES'
print(x)
