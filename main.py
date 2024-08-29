import os
import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return all_data

def linear_read(filenames):
    start_time = time.time()
    for name in filenames:
        read_info(name)
    end_time = time.time()
    print(f"Линейное выполнение заняло: {end_time - start_time:.6f} секунд")

def multiprocess_read(filenames):
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессное выполнение заняло: {end_time - start_time:.6f} секунд")


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    linear_read(filenames)

    multiprocess_read(filenames)
