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

# output:
# initial values [1]
# initial values [1, 2]
# initial values [1, 2, 3]
# after popping values [1, 2]
# after popping values [1]
# after popping values []
