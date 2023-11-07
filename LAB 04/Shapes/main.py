n=input('Enter a number:')
n=int(n)
n=abs(n)
for i in range(n):
    print('\t',n*'*')
x=1
for i in range(n):
    print(f'{x*"*":^{n}}')
    x=x+2
