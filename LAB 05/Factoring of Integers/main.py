Num = int(input('Enter the Number:'))
i = 2
while i <= Num:
    if Num % i == 0:
        Num = Num/i
        print(i)
        i = 2
    else:
        i = i+1
