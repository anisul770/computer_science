import random
Set1 = ['x', 'y']
Set2 = [1, -1]
a = 0
b = 0
for i in range(100):
    n = random.choice(Set1)
    m = random.choice(Set2)
    if n == Set1[0]:
        a = a+m
    if n == Set1[1]:
        b = b+m
print('(', a, ',', b, ')')
