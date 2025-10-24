from multiprocessing import Process, current_process
import time

def compute_heavy_task(task_name, iterations):
    """ Simulates a CPU-Intensive operation  """
    process_name = current_process().name
    print(f"{task_name} started on {process_name}")

    #? Simulate CPU-bound work
    result = 0
    for i in range(iterations):
        result += i **2

        time.sleep(1) #? Additional simulated work
        print(f"{task_name} completed on {process_name}. Result: {result}")
    return result


if __name__ == "__main__":
    start_time = time.time()

    #? Create separate processes for each task
    p1 = Process(target=compute_heavy_task, args=("Task 1", 10000000))
    p2 = Process(target=compute_heavy_task, args=("Task 2", 10000000))
    p3 = Process(target=compute_heavy_task, args=("Task 3", 10000000))

    #? Start all processes (they run on separate CPU cores)
    p1.start()
    p2.start()
    p3.start()

    #? Wait for all processes to complete
    p1.join()
    p2.join()
    p3.join()

    end_time = time.time()
    print(f"\nAll tasks completed in {end_time - start_time:.2f} seconds")