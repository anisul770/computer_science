emty_dic = {}
my_dictionary = {"Romeo":"green","Adam":"purple","Eve":"Blue","Juliet":"Blue"}
name_phone = {"Fred":"4654553","Mary":"6552345","Bob":"56345634","Sarah":"7632636"}
new_dictionary = dict(name_phone)

print(name_phone["Fred"])
if "Pedro" in name_phone:
    print(name_phone["Pedro"])
else:
    print("not in my dictionary")
print(name_phone.get("Pedro","NOT a number"))
name_phone["Pedro"]=6558698677
print(name_phone.get("Mary","NOT a number"))
name_phone["Mary"] = 3333666622
print(name_phone.get("Mary","NOT a number"))
name_phone.pop("Bob")

for key in name_phone:
    print(key,name_phone[key])

for (key,value) in new_dictionary.items():
    print(key,value)

print(new_dictionary.items())
