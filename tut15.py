#tuples in python
country=("India","Russia","switzerland","Maldives","Thailand","Bali","London")
print(country)
print(len(country))
print(country[0])
print(country[6])
print(country[4])
print(country[1:5])
print(country[4:])
print(country[:])
print(country[:7])
print(country[-3:-1])
print(country[-7:-3:2])

if "London" in country:
    print("I will go to London.")
else:
    print("I will definetely go to London.")

if "America" in country:
    print("It is present")
else:
    print("It is absent.")

