names = ['pedro','luis','jacient','julian','maria']
phones=[13123,12323412,124213,345234,3564334634]
names.append('andrea')
phones.append(453454324)
names.insert(1,'cindy')
phones.insert(1,65443435)
if 'cindy' in  names:
    my_index=names.index('cindy')
    names.pop(my_index)
    phones.pop(my_index)
else:
    print('the name is not in the list')
monthly_score=[0]*12
monthsQ=[1,2,3]*4
months=[1,2,3,4,5,6,7,8,9,10,11,12]
print(sum(months))
months2=[i*i for i in range(1,13)]
print(max(months2))
print(min(months2))
print(months2)
print(monthsQ.index(2))
name='Pedro'
print(max(name))
my_list=[12,345,25,345,3,78,3,7,35]
my_list.sort()
print(my_list)
lista=[1,2,3,9,12,10]
print(lista)
lista.sort(reverse=True)
print(lista)
print(lista.pop(2))
name=','.join(name)
print(name)
(lista[1],lista[2])=(lista[2],lista[1])
print(lista)
(a,b,c)=(lista[0],lista[1],lista[2])
print(a,b,c)
