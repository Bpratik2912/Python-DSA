"""
List is a Python’s built-in data structure that can be used as a queue-methods.
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

# output:
# initial values [1]
# initial values [1, 2]
# initial values [1, 2, 3]
# after popping values [2, 3]
# after popping values [3]
# after popping values []
