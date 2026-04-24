def my_generator():
    for i in range(5000):
        yield i

gen=my_generator()
for i in gen:
    print(i)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))