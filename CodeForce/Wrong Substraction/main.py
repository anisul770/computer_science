x=input()
x=x.split(' ')
a=int(x[0])
b=int(x[1])
for i in range(b):
    if a%10!=0:
        a=a-1
    else:
        a=a/10
print(int(a))
