import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(0)

# Generate synthetic time series data
periods = 4  # Number of seasons in a year
years = 5
time = np.arange(1, periods * years + 1)
trend = np.linspace(10, 20, periods * years)  # Linear trend
seasonal_pattern = np.tile([1.2, 0.8, 1.5, 0.5], years)  # Seasonal component
noise = np.random.normal(0, 0.1, size=time.shape)  # Random noise
data = trend * seasonal_pattern + noise

# Create a pandas DataFrame
df = pd.DataFrame({'Time': time, 'Data': data})

# Define the window size for the moving average (should be the length of one period)
window_size = periods

# Calculate the moving average as the trend
df['Trend'] = df['Data'].rolling(window=window_size, center=True).mean()

# Drop NaN values resulting from the moving average calculation
df.dropna(inplace=True)

# Calculate the ratio of actual values to the trend values
df['Ratio'] = df['Data'] / df['Trend']

# Compute the average ratio for each season
seasonal_indices = df.groupby(df['Time'] % periods)['Ratio'].mean()

# Normalize the seasonal indices to have an average of 1
seasonal_indices /= seasonal_indices.mean()

print("Seasonal Indices:")
print(seasonal_indices)

# Plot the original data and the trend
plt.figure(figsize=(12, 6))
plt.plot(df['Time'], df['Data'], label='Original Data', color='blue', alpha=0.6)
plt.plot(df['Time'], df['Trend'], label='Trend (Moving Average)', color='red')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.title('Original Data and Trend')
plt.show()

# Plot the seasonal indices
plt.figure(figsize=(12, 6))
plt.bar(seasonal_indices.index, seasonal_indices.values, color='green')
plt.xlabel('Season')
plt.ylabel('Seasonal Index')
plt.title('Seasonal Indices (Ratio-to-Trend Method)')
plt.show()
