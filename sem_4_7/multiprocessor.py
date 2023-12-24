import multiprocessing
from multiprocessing import Process
from random import randint
import time

sum_ = multiprocessing.Value('i', 0)

start_time = time.time()


def count_sum(start_index, stop_index, result, array_):
    with result.get_lock():
        for i in range(start_index, stop_index):
            result.value += array_[i]
    print(f'Время выполнения процесса - {time.time() - start_time:.8f}')


start = 0
end = 200_000
STEP = 200_000

if __name__ == '__main__':
    array = []
    for i in range(1_000_000):
        array.append(randint(1, 100))
    processes = []
    for i in range(5):
        p = Process(target=count_sum, args=(start, end, sum_, array), daemon=True)
        processes.append(p)
        p.start()
        start += STEP
        end += STEP

    for proc in processes:
        proc.join()
    print(sum_.value)
