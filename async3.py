import asyncio

async def task1():
    print("Task 1 Started.")
    await asyncio.sleep(1)
    print("Task 1 Finished.")

async def task2():
    print("Task 2 Started.")
    await asyncio.sleep(1)
    print("Task 2 Finished.")

async def task3():
    print("Task 3 Started.")
    await asyncio.sleep(1)
    print("Task 3 Finished.")

async def main():
    L= await asyncio.gather(task1(),task2(),task3())
    print(L)

asyncio.run(main())
