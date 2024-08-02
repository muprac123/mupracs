import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(0)  # For reproducibility

# Generate synthetic time series data
time = np.arange(1, 101)
trend = 0.5 * time  # Linear trend
seasonal = 10 * np.sin(0.2 * time)  # Seasonal component
noise = np.random.normal(0, 5, size=time.shape)  # Random noise

data = trend + seasonal + noise

# Create a pandas DataFrame for convenience
df = pd.DataFrame({'Time': time, 'Data': data})

# Define the window size
window_size = 5

# Apply the moving average
df['Moving_Average'] = df['Data'].rolling(window=window_size).mean()

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(df['Time'], df['Data'], label='Original Data', color='blue', alpha=0.6)
plt.plot(df['Time'], df['Moving_Average'], label=f'Moving Average (window={window_size})', color='red')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.title('Trend Fitting Using Moving Average Method')
plt.show()
