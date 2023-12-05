```python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# import data, pull out the 'x' and 'y' columns, convert to numpy arrays
url = 'https://raw.githubusercontent.com/jmyers7/stats-book-materials/main/data/ch11-suggested-problems-data-01.csv'
df = pd.read_csv(url)
x = df['x'].to_numpy()
y = df['y'].to_numpy()

# create powers up to degree 3
x_power = np.column_stack((x, x ** 2, x ** 3))

# fit a linear regression model on the powers
lr = LinearRegression()
lr.fit(X=x_power, y=y)
beta_0, beta = lr.intercept_, lr.coef_

# define a grid for plotting the degree-3 polynomial
grid = np.linspace(-0.5, 2.5)
grid_poly = np.column_stack((grid, grid ** 2, grid ** 3))

# plot the fitted polynomial and the data
plt.plot(grid, beta_0 + grid_poly @ beta)
plt.scatter(x, y, alpha=0.25)
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
```