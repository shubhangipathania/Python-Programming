import asyncio

async def my_async_function():
    await asyncio.sleep(1)
    return "Hello, Async world."

async def main():
    result= await my_async_function()
    print(result)

asyncio.run(main())