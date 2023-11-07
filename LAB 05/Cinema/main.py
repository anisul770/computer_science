buyer=0
i=0
while i<10:
    ticket=int(input('Number of tickets: '))
    if ticket>10-i:
        print('Only',10-i,'tickets are remaining')
    elif ticket<=4:
        buyer=buyer+1
        i=i+ticket
        print('Remaining tickets: ',10-i)
    else:
        print("You can't buy more than 4 tickets")
print('Number of Buyers: ',buyer)
