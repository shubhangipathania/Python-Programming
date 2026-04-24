import time
import asyncio 
import requests


async def function1():
  print("func 1") 
  URL = "https://images.squarespace-cdn.com/content/v1/604ffb544c6d436ffc845808/085b0e6a-10b7-4d70-b58d-6b6c5cd76810/classic-literature.jpg?format=2500w"
  response = requests.get(URL)
  open("instagram.ico", "wb").write(response.content)
   
  return "Harry"
  
async def function2():
  print("func 2") 
  URL = "https://i0.wp.com/nsfordwriter.com/wp-content/uploads/2020/01/Penguin-classics.jpg?w=688&ssl=1"
  response = requests.get(URL)
  open("instagram2.jpg", "wb").write(response.content)
  
async def function3():
  print("func 3")
  URL = "https://www.istockphoto.com/photo/collection-of-books-on-shelves-in-a-second-hand-bookstore-gm1129874777-298635343"
  response = requests.get(URL)
  open("instagram3.ico", "wb").write(response.content)

async def main():
  # await function1()
  # await function2()
  # await function3()
  # return 3
  L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
  print(L)
  # task = asyncio.create_task(function1())
  # # await function1()
  # await function2()
  # await function3()

asyncio.run(main())