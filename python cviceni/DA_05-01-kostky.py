# kap 5, cv. 1: kostky

import pandas as pd
import matplotlib.pyplot as plt

with open("kostky.txt") as kFile:
    k = [int(h.strip()) for h in kFile]

s = pd.Series(k)
s.hist(bins=range(2,13))
plt.show()
