import threading 
import time 

def func(seconds):
    time.sleep(seconds)
    print("Function 1 executed.")


t1=time.perf_counter()
thread1=threading.Thread(target=func,args=[4])
thread2=threading.Thread(target=func,args=[2])
thread3=threading.Thread(target=func,args=[1])
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
t2=time.perf_counter()
print(t2-t1)
