# A simple project to show statistics metrics
The objective of this model is to show how the statistics metrics can be calculated.

Features:
- Mean, Median, Var using Pandas and Numpy
- Covariance and Correlation
- Confidence Interval
- Random Normal Distribution Creation
- Colored terminal text.
- Histplot with KDE.
- T-Test to determine whether there is a significant difference between the means of two samples.
- Paired T-Test as an alternative to T-Test when we have dependency between samples.
- Shapiro test to detect normal distribution.

## Installing using GitHub
- Fork the project into your GitHub
- Clone it into your dektop
```
git clone https://github.com/jacesca/StatisticsConcepts.git
```
- Setup environment (it requires python3)
```
python -m venv venv
source venv/bin/activate  # for Unix-based system
venv\Scripts\activate  # for Windows
```
- Install requirements
```
pip install -r requirements.txt
```

## Run ML model
```
python statisticsPandas.py
python statisticsNumpy.py
python covariance-correlation.py
python ci.py
python ttest.py
python paired-ttest.py
```

## Others
- Proyect in GitHub: https://github.com/jacesca/StatisticsConcepts
- Commands to save the environment requirements:
```
conda list -e > requirements.txt
# or
pip freeze > requirements.txt

conda env export > flask_env.yml
```
- For coding style
```
black model.py
flake8 model.py
```

## Extra documentation
- [ttest_rel](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html)
- [ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)