import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Generate sample data
np.random.seed(0)
x_data = np.linspace(0, 4, 50)
a, b, c = 2.5, 1.3, 0.5
y_data = a * np.exp(b * x_data) + c + 0.5 * np.random.normal(size=x_data.size)

# Define the modified exponential function
def modified_exponential(x, a, b, c):
    return a * np.exp(b * x) + c

# Fit the curve
popt, pcov = curve_fit(modified_exponential, x_data, y_data, p0=(1, 1, 1))

# Get the fitted parameters
a_fit, b_fit, c_fit = popt
print(f"Fitted parameters: a={a_fit}, b={b_fit}, c={c_fit}")

# Generate y values using the fitted parameters
y_fit = modified_exponential(x_data, *popt)

# Plot the data and the fitted curve
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, y_fit, color='red', label='Fitted curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
