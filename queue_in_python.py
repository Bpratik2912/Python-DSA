"""
The queue is a linear data structure that stores items in a First In First Out (FIFO) manner.
With a queue, the least recently added item is removed first.
A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first.

Python Queue can be implemented by the following ways: (1) list (2) collections.deque (3) queue.Queue

"""

# using list
"""
List is a Python’s built-in data structure that can be used as a queue. 
Instead of enqueue() and dequeue(), append() and pop() function is used
"""
my_values = []
my_values.append(1)
print("initial values", my_values)
my_values.append(2)
print("initial values", my_values)
my_values.append(3)
print("initial values", my_values)

my_values.pop(0)
print("after popping values", my_values)
my_values.pop(0)
print("after popping values", my_values)
my_values.pop(0)
print("after popping values", my_values)


# using collections.deque
"""
Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of
container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides
O(n) time complexity.
"""
from collections import deque

my_values = deque()
my_values.append(1)
print("initial values", my_values)
my_values.append(2)
print("initial values", my_values)
my_values.append(3)
print("initial values", my_values)

my_values.popleft()
print("after popping values", my_values)
my_values.popleft()
print("after popping values", my_values)
my_values.popleft()
print("after popping values", my_values)


# using queue.Queue
"""
Queue is built-in module of Python which is used to implement a queue. queue.Queue(maxsize) initializes a variable to
a maximum size of maxsize. A maxsize of zero ‘0’ means a infinite queue. This Queue follows FIFO rule. There are various
functions available in this module: 

maxsize – Number of items allowed in the queue.
empty() – Return True if the queue is empty, False otherwise.
full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
qsize() – Return the number of items in the queue.
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
