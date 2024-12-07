from collections import deque

# Read number of operations
n = int(input())

# Initialize an empty deque
d = deque()

# Perform the operations
for _ in range(n):
    operation = input().strip().split()
    method = operation[0]
    if len(operation) > 1:
        value = operation[1]
        getattr(d, method)(value)  # Call append/appendleft with value
    else:
        getattr(d, method)()  # Call pop/popleft without arguments

# Print the deque elements space-separated
print(" ".join(d))