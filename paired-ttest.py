"""
Paired T-Test
The paired t-test explicitly does not assume that variances are equal.
For a paired t-test, it's crucial that the sample sizes are equal.

Here, you have data regarding the number of downloads for a particular app.
Take a look at the samples: the mean values are nearly identical.
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel


# Read the data
before = pd.read_csv('data/before.csv').squeeze()
after = pd.read_csv('data/after.csv').squeeze()

# Plot histograms
plt.figure()
plt.hist(before, alpha=0.7, label='Before')
plt.hist(after, alpha=0.7, label='After')
plt.axvline(before.mean(), color='blue', linestyle='dashed')
plt.axvline(after.mean(), color='gold', linestyle='dashed')
plt.legend()

# Confirming if they have the same size
assert len(before) == len(after)
print(f'Sample size >> Before: {len(before)}, After: {len(after)}')

# H₀: The mean number of downloads before and after the changes is the same.
# Hₐ: The mean number of downloads is greater after the modifications.
stats, pvalue = ttest_rel(after, before, alternative='greater')
if pvalue > 0.05:
    print("We support the null hypothesis, the mean values are equal")
else:
    print("We reject the null hypothesis, the mean values are different")

plt.show()
