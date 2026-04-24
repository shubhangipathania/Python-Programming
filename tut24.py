#Dictionary in python
dict1={"Rahul":"CS","Sneha":"BCA","Harsh":"BBA","Ram":"AIML","Tarun":"CA","Kritika":"BCOM"}
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1["Sneha"])
print(dict1["Harsh"])
print(dict1.get("Ram"))
print(dict1.get("Rahul"))
for keys in dict1.keys():
    print(f"The value corresponding to {keys} are {dict1[keys]}")

dict1["Tarun"]="BCOM"
print(dict1)

