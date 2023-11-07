#convert decimal numbers to binanry

Number=int(input('Enter a Number'))
tmp = Number
result=''
while tmp>0:
    rem=tmp%2
    tmp=tmp//2
    result=str(rem)+result
    print(f'Q={tmp} Remainder={rem}')
print('Result',result)
#for i in range(len(result)-1,-1,-1):
#    print(result[i],end='')
#x=len(result)
#print()
#for i in range(len(result)):
#    print(result[x-1],end='')
#    x=x-1
