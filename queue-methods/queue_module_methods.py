"""
Queue is built-in module of Python which is used to implement a queue-methods. queue-methods.Queue(maxsize) initializes a variable to
a maximum size of maxsize. A maxsize of zero ‘0’ means a infinite queue-methods. This Queue follows FIFO rule. There are various
functions available in this module:

maxsize – Number of items allowed in the queue-methods.
empty() – Return True if the queue-methods is empty, False otherwise.
full() – Return True if there are maxsize items in the queue-methods. If the queue-methods was initialized with maxsize=0 (the default), then full() never returns True.
get() – Remove and return an item from the queue-methods. If queue-methods is empty, wait until an item is available.
get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
put(item) – Put an item into the queue-methods. If the queue-methods is full, wait until a free slot is available before adding the item.
put_nowait(item) – Put an item into the queue-methods without blocking. If no free slot is immediately available, raise QueueFull.
qsize() – Return the number of items in the queue-methods.
"""
from queue import Queue

my_values = Queue(maxsize = 3)
my_values.put(1)
print("initial values", my_values.queue)
my_values.put(2)
print("initial values", my_values.queue)
my_values.put(3)
print("initial values", my_values.queue)
print("Full: ", my_values.full())

my_values.get()
print("after popping values", my_values.queue)
my_values.get()
print("after popping values", my_values.queue)
print("Empty: ", my_values.empty())
my_values.get()
print("after popping values", my_values.queue)
print("Empty: ", my_values.empty())

# output:
# initial values deque([1])
# initial values deque([1, 2])
# initial values deque([1, 2, 3])
# Full:  True
# after popping values deque([2, 3])
# after popping values deque([3])
# Empty:  False
# after popping values deque([])
# Empty:  True
