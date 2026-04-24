info={1:"SHUBH",2:"OM",3:"ABHISHEK",4:"RIYA",5:"ISHA"}
info2={6:"NEHA",7:"SHIKHA"}
info.update(info2)
info.update({8:"MANAS"})
print(info)
info2.clear()
print(info2)
info.pop(5)
print(info)
info.popitem()
print(info)
del info2
#print(info2)