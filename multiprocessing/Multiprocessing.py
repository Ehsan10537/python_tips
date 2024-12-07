import time
import multiprocessing

def square_numbers():
    for num in range(5):
        time.sleep(1)
        print(f"square: {num*num}")

def cube_numbers():
    for num in range(5):
        time.sleep(1.5)
        print(f"cubed: {num*num*num}")

if __name__ == '__main__':
    # Create 2 processes
    process_1 = multiprocessing.Process(target=square_numbers)
    process_2 = multiprocessing.Process(target=cube_numbers)

    # Capture the start time
    start_time = time.time()

    # Start the processes to run
    process_1.start()
    process_2.start()

    # join the processes
    process_1.join()
    process_2.join()

    # Capture the time it ends and calculate the execution time.
    finishing_time = time.time()
    execution_time = finishing_time - start_time
    print('Execution time applying multiprocessing:', execution_time)
