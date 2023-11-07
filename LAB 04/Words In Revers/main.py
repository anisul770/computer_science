Word=input('Type your word:')
x=y=len(Word)
for i in range(x):
    print(Word[x-1],end='')
    x=x-1
print()
for j in range(y):
    if Word[y-1].isupper()==True:
        print(Word[y-1],end='')
    y=y-1
