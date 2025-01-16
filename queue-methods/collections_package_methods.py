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

# output:
# initial values deque([1])
# initial values deque([1, 2])
# initial values deque([1, 2, 3])
# after popping values deque([2, 3])
# after popping values deque([3])
# after popping values deque([])
