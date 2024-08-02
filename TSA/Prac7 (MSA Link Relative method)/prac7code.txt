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

# Calculate Link Relatives
df['Link_Relative'] = df['Sales'] / df['Sales'].shift(1)

# Set NaN for the start of each year using `loc`
df.loc[df.groupby('Year').head(1).index, 'Link_Relative'] = np.nan

# Calculate Average Link Relatives
average_link_relatives = df.groupby('Month')['Link_Relative'].mean()

# Adjusting so the average of indices is 100
average_link_relatives = average_link_relatives.fillna(1)  # Replace NaN with 1 for calculation
seasonal_indices = (average_link_relatives / average_link_relatives.mean()) * 100

print(seasonal_indices)
