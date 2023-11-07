Number=input('Enter a Number:')
Number=int(Number)
if Number==2 :
    print('2 Is Prime')
elif Number>2:
       x=False
       i=2
       while i<=Number/2 and x==False:
           if Number%i==0:
             x=True
           i=i+1
       if x==True:
        print(Number,'Is Not Prime')
       else:
        print(Number,'Is Prime')
else:
    print(Number,'Is Not Prime')
