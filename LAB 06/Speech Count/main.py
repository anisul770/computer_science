def count_vowels(string):
    x=string.split(' ')
    length=len(x)
    count=0
    Set={'a','e','i','o','u','A','E','I','O','U'}
    for i in range(length):
        for j in range(len(x[i])):
           k=x[i]
           if k[j] in Set:
              count=count+1
    print('Number of vowels:',count)
Speech=input('Type your Speech:')
count_vowels(Speech)
