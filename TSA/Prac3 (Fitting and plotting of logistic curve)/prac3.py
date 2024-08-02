import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def logistic(t, L, k, t0):
    return L / (1 + np.exp(-k * (t - t0)))

# Parameters for the true logistic function
L_true = 100
k_true = 0.1
t0_true = 10

# Generate synthetic data
t_data = np.linspace(0, 50, 100)
y_true = logistic(t_data, L_true, k_true, t0_true)
noise = np.random.normal(0, 5, size=t_data.shape)
y_data = y_true + noise

# Initial guess for the parameters
initial_guess = [90, 0.1, 10]

# Fit the curve
popt, pcov = curve_fit(logistic, t_data, y_data, p0=initial_guess)

# Extract the fitted parameters
L_fit, k_fit, t0_fit = popt
print(f"Fitted parameters: L = {L_fit}, k = {k_fit}, t0 = {t0_fit}")

# Generate the fitted curve
y_fit = logistic(t_data, L_fit, k_fit, t0_fit)

# Plot the data and the fitted curve
plt.figure(figsize=(10, 6))
plt.scatter(t_data, y_data, label='Data', color='blue', s=10)
plt.plot(t_data, y_true, label='True Logistic Curve', color='green', linestyle='dashed')
plt.plot(t_data, y_fit, label='Fitted Logistic Curve', color='red')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.title('Logistic Curve Fitting')
plt.show()
