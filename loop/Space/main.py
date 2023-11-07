Number= input('Enter a number:')
A=len(Number)
if A==5:
 for i in str(Number):
    print(i, end='\t')
else:
    print('The number is not 5 digit')
