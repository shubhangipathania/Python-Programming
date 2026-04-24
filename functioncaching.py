from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n

print(fx(2))
print("Done for 2")
print(fx(4))
print("Done for 4")
print(fx(10))
print("Done for 10")
print(fx(20))
print("Done for 20")

print(fx(2))
print("Done for 2")
print(fx(4))
print("Done for 4")