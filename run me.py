from multiprocessing import Process, cpu_count
import time


# first iteration of logic 
def counter(number):
    while number > 0:
        number -= 1
        time.sleep(0.5)

# calls annoying process
def spawn_processes(num_processes):
    processes = [Process(target=counter, args=(1000,)) for _ in range(num_processes)]
    for process in processes:
        process.start()
        print(f"Started {process.pid}.")
    for process in processes:
        process.join()
        print(f"Process {process.pid} has finished.")

def main():
    num_processors = cpu_count()
    num_processes = num_processors * 2  # Adjust the number of processes to spawn as needed.
    print(f"Number of logical processors: {num_processors}")
    print(f"Creating {num_processes} processes.")
    print("Warning: This will consume a lot of system resources, and potentially freeze your PC, make sure to adjust the number of processes and sleep seconds as needed.")
   
    spawn_processes(num_processes)

if __name__ == "__main__":
    main()
# only tested on windows
