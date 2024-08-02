import numpy as np
import pandas as pd

# Example sales data for 3 years (36 months)
np.random.seed(0)
data = {
    'Year': np.repeat([1, 2, 3], 12),
    'Month': list(range(1, 13)) * 3,
    'Sales': np.random.randint(80, 120, size=36)
}
df = pd.DataFrame(data)

# Calculate Differences
df['Difference'] = df['Sales'].diff()

# Remove NaN values resulting from the difference calculation
df = df.dropna()

# Calculate the Variance of Differences
variance_difference = df['Difference'].var()

# Print the Variance of Differences
print("Variance of Differences:", variance_difference)
