N=input('Enter 3 digit number:')
number=N[0:3]
if (number.isdigit()!=True):
    print('You should enter only numbers')
elif int(number[0])<int(number[1]):
    if int(number[1])<int(number[2]):
        print('increasing')
elif int(number[0])>int(number[1]):
    if int(number[1])>int(number[2]):
        print('decreasing')
else:
    print('neither')


