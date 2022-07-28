import random

from sklearn import datasets
from matplotlib import pyplot
import pandas as pd
import numpy as np
from win32com import client
import matplotlib.pyplot as plt
import matplotlib.style

import collections

"""X, y = datasets.load_digits(return_X_y=(True))

X0 = X[0]
X0_square = X0.reshape(8, 8)


fig, ax = pyplot.subplots()
ax.imshow(X0_square, cmap="binary")
AAAAAAAAAAAAAaaaaaaaaaaaaaa
"""

np.random.seed(111)
dates = pd.date_range(start="2020/01/01", periods=365)
df = pd.DataFrame(np.random.randint(1, 31, 365), index=dates, columns=["乱数"])
# print(df.groupby(pd.Grouper(freq="M")).mean())
df1 = df.loc[:, "乱数"].resample("M").mean()
df_year = pd.DataFrame(df.groupby(pd.Grouper(freq="W-SAT")).sum(), columns=["乱数"])
print(df_year.corr())

matplotlib.style.use("ggplot")
x = [1, 2, 3]
y1 = [1, 2, 3]
y2 = [3, 1, 2]

fig, ax = plt.subplots(1)
label = ["a", "b", "c"]
width = 0.4

y_total = [num1 + num2 for num1, num2 in zip(y1, y2)]
x2 = [num + width for num in x]

ax.bar(x, y_total, tick_label=label, label="yt", )
ax.bar(x, y1, tick_label=label, label="y1", width=width)
ax.bar(x2, y2, tick_label=label, label="y2", width=width)
ax.set_title("sample_style")
ax.legend()
plt.show()

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
