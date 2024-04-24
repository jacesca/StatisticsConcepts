"""
Covariance is a measure of the joint variability of two random variables.
The value of covariance	Meaning:
Positive	Two variables move in the same direction
0	        Two variables no linear relationship
Negative	Two variables move in opposite directions

Correlation is a statistical measure that quantifies the degree of association
or relationship between two variables.
The correlation value falls within the range of [-1; 1].
Correlation Value	Meaning
1	        Perfect positive correlation: When one value increases, the other
            also increases, and vice versa.
0	        No correlation: There is no visible relationship between the
            variables.
-1	        Perfect negative correlation: When one value increases, the other
            decreases, and vice versa.
"""
import pandas as pd
import numpy as np

df = pd.read_csv('data/Stores.csv')
print(df.head())

# Calculating covariance
cov = np.cov(df['Store_Area'], df['Items_Available'])[0, 1]

# Calculating correlation
corr = np.corrcoef(df['Store_Area'], df['Items_Available'])[0, 1]

print('Covariance:', round(cov, 4))
print('Correlation:', round(corr, 4))
