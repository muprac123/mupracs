import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gompertz(t, a, b, c):
    return a * np.exp(-b * np.exp(-c * t))

# Parameters for the true Gompertz function
a_true = 100
b_true = 2
c_true = 0.1

# Generate synthetic data
t_data = np.linspace(0, 50, 100)
y_true = gompertz(t_data, a_true, b_true, c_true)
noise = np.random.normal(0, 5, size=t_data.shape)
y_data = y_true + noise

# Initial guess for the parameters
initial_guess = [90, 1, 0.1]

# Fit the curve
popt, pcov = curve_fit(gompertz, t_data, y_data, p0=initial_guess)

# Extract the fitted parameters
a_fit, b_fit, c_fit = popt
print(f"Fitted parameters: a = {a_fit}, b = {b_fit}, c = {c_fit}")

# Generate the fitted curve
y_fit = gompertz(t_data, a_fit, b_fit, c_fit)

# Plot the data and the fitted curve
plt.figure(figsize=(10, 6))
plt.scatter(t_data, y_data, label='Data', color='blue', s=10)
plt.plot(t_data, y_true, label='True Gompertz Curve', color='green', linestyle='dashed')
plt.plot(t_data, y_fit, label='Fitted Gompertz Curve', color='red')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.title('Gompertz Curve Fitting')
plt.show()
