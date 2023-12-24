import threading
import time
from random import randint

array = []


for i in range(1_000_000):
    array.append(randint(1, 100))
sum_ = 0


def count_sum(start_index, stop_index, thread_number):
    global sum_
    for i in range(start_index, stop_index):
        sum_ += array[i]
    print(f'Время выполнения потока {thread_number + 1} - {time.time() - start_time:.8f}')


start = 0
stop = 100_000
STEP = 100_000
threads = []
for i in range(10):
    start_time = time.time()
    thread = threading.Thread(target=count_sum, args=(start, stop, i))
    start += STEP
    stop += STEP
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()
print(sum_)






