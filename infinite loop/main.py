Number = input("Enter the Name:")
A = len(Number)
if A >= 6:
    print(f'{Number[0:3]}...{Number[-3:]}')
elif 3 < A < 6:
    print(f'{Number[0:3]}...')
else:
    print(f'{Number[0:3]}')
