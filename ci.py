"""Confidence Interval"""
# Importing libraries
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


CRED = '\033[42m'
CEND = '\033[0m'

print(CRED + 'Example 1' + CEND)
# Creating random normal distribution
dist = st.norm.rvs(size=1000, loc=50, scale=2)

# Finding confidence interval
confidence = st.norm.interval(confidence=0.95, loc=np.mean(dist),
                              scale=st.sem(dist))
print(confidence)

# Create the histplot
plot = sns.histplot(x=dist, kde=True, )
plot.set_title('Normal Distribution')
plot.set(xlabel='Data', ylabel='The Quantity')

print(CRED + 'Example 2' + CEND)
# If we are working with a small distribution (size less than or equal to 30)
# that approximates the normal distribution, we will use t-statistics.
data = [104, 106, 106, 107, 107, 107, 108, 108, 108, 108, 108, 109, 109, 109,
        110, 110, 111, 111, 112]
confidence = st.t.interval(confidence=0.95,
                           df=len(data)-1,
                           loc=np.mean(data),
                           scale=st.sem(data))
print(confidence)


plt.show()
