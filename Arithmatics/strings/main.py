import math
friend="anis"
print(friend)
print(len(friend))
print(friend[0])
r=12
pi=3.14
area= (r**2)*pi
print("The area of a circle of radius %f is %f" %(r,area))
print("The area of a circle of radius "+str(r)+' is '+str(area))
print(f"The area of a circle of radius {r} is {area}")

name="NAME"
surn="Last Name"
ID="ID Number"

Name1="Pedro"
Lastn1="Ramirez"
ID1=123456

print(F"{name:^10}{surn:^15}{ID:^10}")
print(F"{Name1:<10}{Lastn1:<15}{ID1:>10}")
print(F"{Name1:<10}{Lastn1:<15}{ID1:>10}")
print(F"{Name1:<10}{Lastn1:<15}{ID1:>10}")
print(F"{Name1:<10}{Lastn1:<15}{ID1:>10}")
print(F"{Name1:<10}{Lastn1:<15}{ID1:>10}")
