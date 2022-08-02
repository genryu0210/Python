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
df = pd.DataFrame(data=[[0, 1, 2, 3], [4, 5, 6, 7]], columns=["a", "b", "c", "d"], index=["01", "02"])
df["e"] = 0

df["e"][1] = 4


print(df)
