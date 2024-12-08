from concurrent.futures import ProcessPoolExecutor
import time

def func(n):
    time.sleep(2)
    return n*n

if __name__ == '__main__':
    start_time = time.time()

    with ProcessPoolExecutor(max_workers=5) as executor:  # define the number of processes in the pool
        futures = [executor.submit(func, i) for i in range(15)]

    end_time = time.time()
    print(f"execution time with submit method:", end_time-start_time)

    print("\n\n results for submit method:  ")
    for future in futures:
        print(future.result())

