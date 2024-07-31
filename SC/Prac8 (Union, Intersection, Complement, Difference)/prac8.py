import numpy as np
import matplotlib.pyplot as plt

# Define the fuzzy sets 
setA = np.array([0.1, 0.4, 0.7, 0.])
setB = np.array([0.2, 0.5, 0.8])

# Define the universe of Discourse 
x = np.linspace(0, 1, 100)

# Define the membership functions 
mA = np.interp(x, [0, 0.5, 1], [0, 1, 0])
mB = np.interp(x, [0, 0.5, 1], [0, 1, 0.5])

# Perform Union 
union = np.fmax(mA, mB)

# Perform Intersection 
intersection = np.fmin(mA, mB)

# Perform Complement 
complementA = 1 - mA

# Perform Difference 
diff = np.fmax(mA - mB, np.zeros_like(x))

# Plot the fuzzy sets and the operations 
plt.figure(figsize=(10, 8))

plt.plot(x, mA, label="A")
plt.plot(x, mB, label="B")
plt.plot(x, union, label="A union B")
plt.plot(x, intersection, label="A intersection B")
plt.plot(x, complementA, label="A Complement")
plt.plot(x, diff, label="A difference B")

plt.legend(loc="upper right")
plt.show()
