#creating a thread  

import threading
import time

def task(name):
   print(f"Thread {name} starting")
   time.sleep(2)
   print(f"Thread {name} finished")

# Create threads
t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

# Start threads
t1.start()
t2.start()

print(t1.is_alive())
print(t2.is_alive())
# Wait for threads to complete
t1.join()
t2.join()

#creating multiple turns


def print_numbers():
   for i in range(5):
       print(i)

def print_letters():
   for ch in ['A', 'B', 'C', 'D']:
       print(ch)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

# creating threads using locks


lock = threading.Lock()
counter = 0

def increment():
   global counter
   for _ in range(1000):
       with lock:
           counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]

for t in threads:
   t.start()

for t in threads:
   t.join()

print(counter)              

#create threads with arguments

def greet(name):
   print(f"Hello {name}")

t = threading.Thread(target=greet, args=("Alice",))
t.start()
t.join()

#naming the threads

def greet(name):
   print(f"Hello {name}")

t = threading.Thread(target=greet, args=("Alice",))
t.start()
t.join()

# Daemon Threads (Background threads )

import threading
import time

def background():
   while True:
       print("Running in background")
       time.sleep(1)

t = threading.Thread(target=background, daemon=True)
t.start()

time.sleep(3)
print("Main thread ends")



#=============================================synchronisation========================================================================

#using lock

counter = 0
lock = threading.Lock()

def increment():
   global counter
   for _ in range(100000):
       lock.acquire()
       counter += 1
       lock.release()

threads = []

for _ in range(2):
   t = threading.Thread(target=increment)
   threads.append(t)
   t.start()

for t in threads:
   t.join()

print(counter)

#RLock (Re entrant Lock)
# ----> lock = threading.RLock()

#SemaPhore

import time

sem = threading.Semaphore(2)

def task(name):
   with sem:
       print(f"{name} accessing resource")
       time.sleep(2)

for i in range(5):
   threading.Thread(target=task, args=(i,)).start()

#Event

import threading

event = threading.Event()

def waiter():
   print("Waiting...")
   event.wait()
   print("Done waiting!")

def setter():
   print("Setting event")
   event.set()

threading.Thread(target=waiter).start()
threading.Thread(target=setter).start()

#condition

condition = threading.Condition()
items = []

def producer():
   with condition:
       items.append(1)
       print("Produced")
       condition.notify()

def consumer():
   with condition:
       condition.wait()
       print("Consumed", items.pop())

threading.Thread(target=consumer).start()
threading.Thread(target=producer).start()

#Barrier

barrier = threading.Barrier(3)

def task(n):
   print(f"Thread {n} waiting")
   barrier.wait()
   print(f"Thread {n} passed")

for i in range(3):
   threading.Thread(target=task, args=(i,)).start()


#=============================================================================thread pool====================================================

from concurrent.futures import ThreadPoolExecutor

def task(n):
   return f"Task {n} done"

with ThreadPoolExecutor(max_workers=3) as executor:
   results = executor.map(task, range(5))

for r in results:
   print(r)


# Using Submit Function

from concurrent.futures import ThreadPoolExecutor

def square(n):
   return n * n

with ThreadPoolExecutor(max_workers=2) as executor:
   future1 = executor.submit(square, 4)
   future2 = executor.submit(square, 5)

   print(future1.result())
   print(future2.result())


# Using as_completed

from concurrent.futures import ThreadPoolExecutor, as_completed

def work(n):
   return n * 2

with ThreadPoolExecutor(max_workers=3) as executor:
   futures = [executor.submit(work, i) for i in range(5)]

   for future in as_completed(futures):
       print(future.result())
