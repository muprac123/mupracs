import numpy as np

# Enter Data
u = np.array(eval(input('Enter First Matrix (as a Python list): ')))
v = np.array(eval(input('Enter Second Matrix (as a Python list): ')))

# Perform Operations
w = np.maximum(u, v)  # Union
p = np.minimum(u, v)  # Intersection
q1 = 1 - u           # Complement of First Matrix
q2 = 1 - v           # Complement of Second Matrix

# De Morgan's Law
# Left-hand side
x1 = 1 - w           # Complement of Union
# Right-hand side
x2 = np.minimum(q1, q2)  # Intersection of Complements

# Left-hand side 1
y1 = 1 - p           # Complement of Intersection
# Right-hand side 1
y2 = np.maximum(q1, q2)  # Union of Complements

# Display Output
print('Union of Two Matrices:')
print(w)

print('Intersection of Two Matrices:')
print(p)

print('Complement of First Matrix:')
print(q1)

print('Complement of Second Matrix:')
print(q2)

print('De-Morgan\'s Law:')
print('LHS:')
print(x1)
print('RHS:')
print(x2)
print('LHS1:')
print(y1)
print('RHS1:')
print(y2)
