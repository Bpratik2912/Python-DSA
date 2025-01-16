"""
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.
In stack, a new element is added at one end and an element is removed from that end only.
The insert and delete operations are often called push and pop.

Stack in Python can be implemented using the following ways: (1) list (2) Collections.deque (3) queue.LifoQueue
"""

# using List
"""
Python’s built-in data structure list can be used as a stack. 
Instead of push(), append() is used to add elements to the top of the stack while pop() removes the element in LIFO order.
"""
my_values = []

my_values.append(1)
print("initial values", my_values)
my_values.append(2)
print("initial values", my_values)
my_values.append(3)
print("initial values", my_values)

my_values.pop()
print("after popping values", my_values)
my_values.pop()
print("after popping values", my_values)
my_values.pop()
print("after popping values", my_values)


# using Collections.deque
"""
Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends of the 
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

my_values.pop()
print("after popping values", my_values)
my_values.pop()
print("after popping values", my_values)
my_values.pop()
print("after popping values", my_values)


# using queue.Queue
"""
Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using the
put() function and get() takes data out from the Queue. 

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
from queue import LifoQueue

my_values = LifoQueue(maxsize = 3)
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