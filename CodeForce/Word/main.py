x=input()
a=0
b=0
for i in range(len(x)):
    if x[i].isupper()==True:
        a=a+1
    else:
        b=b+1
if a>b:
    print(x.upper())
else:
    print(x.lower())
