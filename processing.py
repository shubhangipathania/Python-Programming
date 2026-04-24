import multiprocessing

def task1():
    print("Hello from process", multiprocessing.current_process().name)


def task2():
    print("Hello from process", multiprocessing.current_process().name)

if __name__== '__main__':
    process1= multiprocessing.Process(target = task1)
    process2= multiprocessing.Process(target = task2)
    process1.start()
    process2.start()
    process1.join()
    process2.join()



