import numpy as np

def exponential_smoothing(data, alpha):
    """
    Perform exponential smoothing forecasting.

    :param data: List of historical data points.
    :param alpha: Smoothing constant (between 0 and 1).
    :return: Forecast for the next period and smoothed values.
    """
    # Initialize the smoothed values array
    smoothed_values = np.zeros(len(data))
    
    # Set the initial smoothed value (first data point)
    smoothed_values[0] = data[0]
    
    # Calculate the smoothed values for each period
    for t in range(1, len(data)):
        smoothed_values[t] = alpha * data[t-1] + (1 - alpha) * smoothed_values[t-1]

    # The forecast for the next period (Month 7) should be the last smoothed value
    forecast = smoothed_values[-1]

    return forecast, smoothed_values

# Historical sales data
sales_data = [120, 130, 125, 140, 150, 145]

# Smoothing constant
alpha = 0.3

# Perform exponential smoothing
forecast, smoothed_values = exponential_smoothing(sales_data, alpha)

print(f"Smoothed Values: {smoothed_values}")
print(f"Forecast for Month 7: {forecast:.3f} units")
