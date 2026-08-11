# import asyncio
# import random

# async def simulated_download(task_id):
#     wait_time = random.randint(1, 3)
#     print(f"Download {task_id} started (will take {wait_time}s).")
#     await asyncio.sleep(wait_time)
#     print(f"Download {task_id} completed!")
#     return f"Data from {task_id}"

# async def main():
#     # Step 1: Fire off tasks into the background immediately
#     tasks = []
#     for i in range(1, 4):
#         task = asyncio.create_task(simulated_download(f"File_{i}"))
#         tasks.append(task)
#         print(tasks)
#     print("All tasks have been scheduled to run in the background!")
    
#     # Step 2: Extract results as they finish by awaiting the task objects
#     for task in tasks:
#         result = await task
#         print(f"Main received: {result}")

# asyncio.run(main())
import asyncio
import random

async def simulated_download(task_id):
    # Randomly takes 1, 2, or 3 seconds
    wait_time = random.randint(1, 3)
    print(f"Download {task_id} started (will take {wait_time}s).")
    await asyncio.sleep(wait_time)
    print(f"Download {task_id} completed!")
    return f"Data from {task_id} (took {wait_time}s)"

async def main():
    # 1. Create and schedule the tasks
    tasks = [asyncio.create_task(simulated_download(f"File_{i}")) for i in range(1, 4)]
    
    print("All tasks scheduled! Processing them as they finish...\n")
    
    # 2. Use as_completed to yield tasks in order of completion
    for finished_task in asyncio.as_completed(tasks):
        result = await finished_task
        print(f"Main received: {result}")

asyncio.run(main())
