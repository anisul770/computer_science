Try=1
while Try<4:
    PIN=int(input('Enter your PIN:'))
    if PIN==1234:
        print('your pin is correct')
        exit()
    else:
        print('your pin is incorrect')
    Try=Try+1
if Try==4:
    print('Your Bank card is blocked')
