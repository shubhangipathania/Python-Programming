n1={"harsh","Riya","Sakshi","Shivam","anu","Aru"}
n2={"shreya","Riya","Rohan","Prapti","Shivam"}
print(n1.union(n2))
print(n1.intersection(n2))
print(n1.symmetric_difference(n2))
print(n1.difference(n2))
print(n2.difference(n1))
# n1.update(n2)
# n1.intersection_update(n2)
#n1.symmetric_difference_update(n2)
n1.difference_update(n2)
print(n1)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# cities4=cities.intersection(cities2)
# print(cities3)
# print(cities4)
# cities.intersection_update(cities2)
# print(cities)


