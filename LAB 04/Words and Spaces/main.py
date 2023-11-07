Word=input('Type your word:')
length=len(Word)
for i in range(length):
    print(Word[i])
j=0
k=1
l=2
while j<length:
 for i in range(length):
    if i<length-k:
     print(Word[i:i+l])
 j=j+1
 k=k+1
 l=l+1
