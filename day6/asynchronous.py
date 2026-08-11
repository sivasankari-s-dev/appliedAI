import asyncio

async def greet(name,delay):
    await asyncio.sleep(delay)
    print(f"Hi, {name}!")

async def main():
    name = input("What is your name? ")
    delay = float(input("Enter delay in seconds: "))
    await greet(name, delay)

asyncio.run(main())