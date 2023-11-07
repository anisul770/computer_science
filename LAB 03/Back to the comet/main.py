from math import*

v = float(sqrt((2*6.67*pow(10, -11)*2.2*pow(10, 14))/(9400/2)))
v = round(v, 2)
speed = float(input("Enter the Speed:"))
speed = round(speed, 2)
if speed >= v:
    print('He will not be able to return to the surface')
    mass = (pow(v, 2)*9400/2)/(2*6.67*pow(10, -11))
    mass = mass - (2.2*pow(10, 14))
    print('The comet have to be ', round(mass, 2), 'kg heavier then before to return to the surface')
else:
    print('He will be able to return the surface')

print(v, speed)
