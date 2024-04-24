# Import library
import numpy as np
import pandas as pd

df = pd.read_csv('data/ds_salaries_statistics.csv', index_col=0)
print(df.head())

# Calculate the mean value
mean = np.mean(df['salary_in_usd'])

# Calculate the median value
median = np.median(df['salary_in_usd'])

# Calculate the variance using the function from the NumPy library
var = np.var(df['salary_in_usd'])

# Calculate the standard deviation using the function from the NumPy library
std = np.std(df['salary_in_usd'])

print('The mean value is', mean)
print('The median value is', median)
print('The variace using NumPy library is', var)
print('The standard deviation using NumPy library is', round(std, 2))
