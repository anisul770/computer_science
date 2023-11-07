A = input("Type something:")
if A.isdigit():
    print('{} is all digit'.format(A))
elif A.isalpha():
    if A.isupper():
        print(A, 'All capital letters')
    elif A.islower():
        print(A, 'Only lower case')
    elif A[0].islower():
        print(A, "it starts with a lower case")
    else:
        print(A, 'Only letters')
elif A[-1] == '.':
    print(A, 'it ends with a point')
else:
    print('{} is letters and numbers'.format(A))
