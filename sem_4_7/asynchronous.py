import asyncio
from random import randint
import time

start_time = time.time()
arr = []


async def create_array():
    global arr
    for i in range(100):
        arr.append(randint(1, 100))


async def array_sum():
    sum_ = 0
    for i in arr:
        sum_ += i
    print(f'Время выполнения {time.time() - start_time:.8f}, сумма - {sum_}')


async def main():
    task1 = asyncio.create_task(create_array())
    task2 = asyncio.create_task(array_sum())
    await task1
    await task2


asyncio.run(main())
