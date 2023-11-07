username=input()
lenght=len(username)
Set=set()
for i in range(lenght):
    Set.add(username[i])
if len(Set)%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
