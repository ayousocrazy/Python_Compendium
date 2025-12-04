from threading import *
import time

start = time.time()

def download():
    print("Downloading file")
    time.sleep(1)
    print("Download complete")

for _ in range(6):
    download()

print("Total Time: ", time.time() - start)

"""
Output:
Downloading file
Download complete
Downloading file
Download complete
Downloading file
Download complete
Downloading file
Download complete
Downloading file
Download complete
Downloading file
Download complete
Total Time:  6.008183002471924

Since they run one after another, total time ≈ 6 seconds
"""

# -------------------------------------------------------------------------------------------------------------------------

del download
start = time.time()

threads = []

def download():
    print("Downloading file")
    time.sleep(1)
    print("Download complete")

for _ in range(6):
    t = Thread(target=download) # Create a thread
    threads.append(t)
    t.start() # start the thread 

for t in threads:
    t.join() # wait for thread to join

print("Total time: ", time.time() - start)

"""
Output:
Downloading file
Downloading file
Downloading file
Downloading file
Downloading file
Downloading file
Download complete
Download complete
Download complete
Download complete
Download complete
Download complete
Total time:  1.0073797702789307

We executed all iterator of loop on different thread at a time so the total time got reduced
In this multithreaded version:
- We create 6 separate threads, each running download()
- Each thread starts immediately after t.start()
- All threads sleep simultaneously for 1 second
- join() ensures the main program waits until all threads finish

Because the threads run concurrently, the total time is ≈ 1 second

Python has a Global Interpreter Lock (GIL) that allows only one thread to execute Python bytecode at a time

time.sleep() releases the GIL
Meaning:
Thread 1 starts sleep → releases GIL
Thread 2 starts sleep → releases GIL
Thread 3 starts sleep → releases GIL
"""

# -------------------------------------------------------------------------------------------------------------------------

class Search(Thread): # inheriting from Thread
    def run(self): # run method is expected
        for _ in range(4):
            self.search_start() # access other method usinf run for multithreading

    def search_start(self): # using this directly executes in the main thread
        print("Searching")
        time.sleep(1)
        print("Found!")

class Run(Thread):
    def run(self):
        for _ in range(4):
            self.run_start()

    def run_start(self):
        print("Compiling")
        time.sleep(1)
        print("Running!")

s1 = Search()
r1 = Run()

s1.start() # .start() doesn't execute run() directl
time.sleep(0.2)
r1.start() # .start() starts a new thread and calls run() on it

s1.join()
r1.join()

print("Job Done")

"""
Output:
Searching
Compiling
Found!
Searching
Running!
Compiling
Found!
Searching
Running!
Compiling
Found!
Searching
Running!
Compiling
Found!
Running!
Job Done
"""

# -------------------------------------------------------------------------------------------------------------------------

thread = []

i = 1

def loop():
    global i
    print(f"Loop {i}")
    i += 1

for _ in range(6):
    t = Thread(target=loop)
    threads.append(t)
    t.start() 

for t in threads:
    t.join()

"""
Output:
Loop 1
Loop 2
Loop 2
Loop 3
Loop 4
Loop 6

When multiple threads access shared data → incorrect results (Race Condition)
"""

# -------------------------------------------------------------------------------------------------------------------------

thread = []

l = Lock() # Used to prevent race condition

i = 1

def locked_loop():
    global i
    with l: # ONLY ONE thread can enter this block at a time
        print(f"Loop {i}")
        i += 1

for _ in range(6):
    t = Thread(target=locked_loop)
    threads.append(t)
    t.start() 

for t in threads:
    t.join()

"""
Output:
Loop 1
Loop 2
Loop 3
Loop 4
Loop 5
Loop 6
"""