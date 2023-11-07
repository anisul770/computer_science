import math
x=input("enter a number:")
print(int(x))
y=input("enter a number:")
print(int(y)+int(x))
z=input("enter a number:")
print(int(x)+int(y)+int(z))
a=input("enter a number:")
print(int(x)+int(y)+int(z)+int(a))
X=int(x)
Y=int(y)+int(x)
Z=int(x)+int(y)+int(z)
A=int(x)+int(y)+int(z)+int(a)
Set=[X,Y,Z,A]
print('Maximum',max(Set),'Minimum',min(Set))
even=0
odd=0
for i in Set:
    if i%2==0:
      even=even+1
    elif i%2==1:
        odd=odd+1
print(even,'values are even')
print(odd,'values are odd')
