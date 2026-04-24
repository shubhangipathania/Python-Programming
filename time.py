import time
t= time.localtime()
formatted_time= time.strftime("%Y-%M-%D  %H:%M:%S",t )
print(formatted_time)
print(time.time())
print(time.sleep(5))
print(time.time())
