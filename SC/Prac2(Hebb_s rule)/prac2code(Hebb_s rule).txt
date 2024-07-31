import numpy as np 

x1 = np.array([1, 1, 1, -1, 1, -1, 1, 1, 1])
x2 = np.array([1, 1, 1, 1, -1, 1, 1, 1, 1])
y = np.array([1, -1])

# Initialize weights and bias
wtold = np.zeros((9,))
bias = 0

print("First input with target=1")
for i in range(0, 9):
    wtold[i] = wtold[i] + x1[i] * y[0]
bias = bias + y[0]
print("Old wt=", wtold)
print("Bias value", bias)

print("Second input with target=-1")
for i in range(0, 9):
    wtold[i] = wtold[i] + x2[i] * y[1]
bias = bias + y[1]
print("New wt=", wtold)
print("Bias value", bias)
