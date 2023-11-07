import random

ordered = []

for i in range(20):
    j = random.randint(0, 99)
    print(j, end=' ')
    ordered.append(j)
print()
ordered = sorted(ordered)
for i in ordered:
    print(i, end=" ")
ordered.reverse()
print()
for i in ordered:
    print(i, end=" ")

