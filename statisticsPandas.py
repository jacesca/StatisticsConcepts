# Import library
import pandas as pd

df = pd.read_csv('data/ds_salaries_statistics.csv', index_col=0)
print(df.head())

# Calculating the mean value
mean = df['work_year'].mean()

# Calculating the median value
median = df['work_year'].median()

# Calculate the variance using the function from the pandas library
var = df['salary_in_usd'].var()

# Calculate the standard deviation using the function from the pandas library
std = df['salary_in_usd'].std()

print('The mean value is', mean)
print('The median value is', median)
print('The variace using pandas library is', var)
print('The standard deviation using pandas library is', round(std, 2))
