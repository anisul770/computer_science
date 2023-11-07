# uk_flag = {'blue', 'red', 'white'}
list_uk_flag = ['blue', 'Red', 'white', 'red', 'white']
uk_flag = set(list_uk_flag)
ca_flag = {'red', 'white'}
it_flag = {'green', 'red', 'white'}

print("Size of set uk_flag: ", len(uk_flag))
print("Size of set list_uk_flag: ", len(list_uk_flag))

if "blue" in ca_flag:
    print("Yes!!")
else:
    ca_flag.add("blue")
for element in uk_flag:
    print(element)
print("------------ ")
for element in sorted(uk_flag):
    print(element)
# uk_flag.discard("Red")
# uk_flag.discard("Red")
uk_flag.remove("Red")
uk_flag.remove("Red")
