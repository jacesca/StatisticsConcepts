"""
T-test is a statistical test used to determine whether
there is a significant difference between the means of two samples.

For it to be true, a few important assumptions are made:
- Homogeneity of Variance. The variances of the two compared groups
        should be approximately the same.
- Normality. Both samples should roughly follow a Normal distribution.
- Independence. The samples need to be independent, implying that the
        values in one group shouldn't be influenced by those in the
        other group.
It's important to note that the t-test may yield inaccurate results
if these assumptions are not met.

There are different types of t-tests that handle violations of some
of the assumptions:
- If the variances are different, you can run Welch's t-test.
        Its idea is the same. The only thing that differs is the degrees
        of freedom. Performing Welch's t-test instead of the ordinary
        t-test in Python is as easy as setting equal_var=False.
- If samples are not independent(for example, if you want to compare the
        means of the same group at different time periods), you can run
        a paired t-test.
In Summary:
Normality, Homogeneity but no Independence >> Paired t-test
Normality, Homogeneity, Independence       >> Regular t-test
Normality, Independence but no Homogeneity >> Welch's t-test
"""
import pandas as pd
from scipy.stats import shapiro, levene, ttest_ind


CRED = '\033[42m'
CEND = '\033[0m'

# Load the data
male = pd.read_csv('data/male.csv').squeeze()
female = pd.read_csv('data/female.csv').squeeze()

# Assuming both datasets are independent.
# Confirming if they follow a normal distribution:
for label, data in {'male': male, 'female': female}.items():
    stat_control, p_value = shapiro(data)
    if p_value > 0.05:
        print(f'{label} dataset is likely to normal distribution')
    else:
        print(f'{label} dataset is NOT likely to normal distribution')

# Verifying the homogeneity of variance
statistic, p_value = levene(male, female)
if p_value > 0.05:
    print('The variances of the two groups are NOT statistically different')  # noqa
else:
    print('The variances of the two groups are statistically different')  # noqa

# Apply t-test
# Considering the alternative parameter (the type of alternative hypothesis):
# 'two-sided' — indicates that the means are not equal.
# 'less'      — implies that the first mean is less than the second.
# 'greater'   — implies that the first mean is greater than the second.
# We have the hypothesis:
# Ho: Females and Males have the same height.
# H1: Males are taller.
t_stat, pvalue = ttest_ind(male, female, equal_var=True,
                           alternative="greater")

# Check if we should support or not the null hypothesis if pvalue > 0.05:
if pvalue > 0.05:
    print(CRED + "We support the null hypothesis, the mean values are equal" + CEND)  # noqa
else:
    print(CRED + "We reject the null hypothesis, males are taller" + CEND)
