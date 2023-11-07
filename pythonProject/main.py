pin = "1234"
A = input("enter your pin ")
if A==pin:
    print("Your pin is correct")
else:
    b=0
    while b<2:
        print("your pin is incorrect")
        A = input("enter your pin")
        if A == pin:
            print("your pin is correct")
            break
        else: b += 1
        print("your bank card is blocked")
