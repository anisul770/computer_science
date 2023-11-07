import random

my_list = [1, 2, 3, 4, 5]
my_list[2] = 8.7676
print(my_list)
names = ['pedro', 'luis', 'jacient', 'julian', 'maria']
phones = [13123, 12323412, 124213, 345234, 3564334634]
agenda = ['pedro', 13123, 'luis', 124213, 'jacient', 345234, 'julian', 12323412, 'maria', 3564334634]
for i in range(len(names)):
    print(names[i], phones[i])
for i in range(0, len(agenda), 2):
    print(agenda[i], agenda[i+1])
my_list2 = [1, 4, 3, 35, 53, 424, 34, 4, 345, 34, 34]
my_list3 = [1, 4, 3, 35, 53, 424, 34, 4, 345, 34, 34]
print(my_list2)
for i in my_list2:
    print(i, end=' ')
print()
for element in my_list3:
    element = element-1
    print(element, end=' ')
print()
for i in range(len(my_list2)):
    my_list2[i] = my_list2[i]-1
    print(my_list2[i], end=' ')
print()
my_list3.insert(3, 4000)
print(my_list3)
print(my_list2)


