info={"NAme":"Arjun", "marks":90,"Class":12,"Branch":"CSE"}
print(info.items())
for keys,values in info.items():
    print(keys,values)

info.update({"marks":95})
print(info)
info.update({"College":"IPEC"})
print(info)
#info.clear()
#print(info)
info.pop("Class")
print(info)
info.popitem()
print(info)