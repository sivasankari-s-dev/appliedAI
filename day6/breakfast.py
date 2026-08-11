import asyncio
import time

async def make_toast():
    print("Making toast...")
    await asyncio.sleep(1.5)  # Simulate time taken to make toast
    print("Toast is ready!")

async def make_coffee():
    print("Making coffee...")
    await asyncio.sleep(3)  # Simulate time taken to make coffee
    print("Coffee is ready!")

async def main():
    start_time = time.time()
    await asyncio.gather(make_toast(), make_coffee())
    end_time = time.time()
    print(f"Breakfast is finished in {end_time - start_time:.2f} seconds.")

asyncio.run(main())