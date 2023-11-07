A = input('Type 20 characters DNA sequence:')
b = input('type 3 characters DNA sequence:')
A = A.upper()
b = b.upper()
e = b[0:3]
a = A[0:20]
print("Long sequence is ", a, '\nShort sequence is ', e)
h = a.find(e)
if h != -1:
    c = a.replace(e, '')
    d = 20-len(c)
    print('The "long sequence" contains the "short sequence"')
    print('In', h+1, 'position of the "long sequence" the "short sequence" starts')
    print('Short sequence appears ', int(d/3), 'times in long sequence')
else:
    print('There is no match')



