Word=input('Type your word:')
length=len(Word)
length=length//2
k=0
l=1
for i in range(length+1):
    if k<len(Word):
     print(Word[k],end='')
    if l<len(Word):
     print(2*Word[l],end='')
    k=k+2
    l=l+2
