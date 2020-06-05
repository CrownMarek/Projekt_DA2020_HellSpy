# kap 5, cv. 2: callcentrum

import pandas as pd
import matplotlib.pyplot as plt

##### varianta 1: pocitani mimo Pandas:

l = []
with open("callcentrum.txt") as cFile:
    for timeStamp in cFile:
        m, s = timeStamp.split(':')
        l.append(int(m) * 60 + int(s))

s = pd.Series(l)

s.hist(bins=range(0, 2100, 10))
plt.show()

s.plot(kind='box', whis=[0, 100])
plt.show()

##### varianta 2: pocitani v Pandas:

s = pd.read_csv("callcentrum.txt", names=['min', 'sec'], sep=":")
sSec = s['min'] * 60 + s['sec']

sSec.hist(bins=range(0, 2100, 10))
plt.show()

sSec.plot(kind='box', whis=[0, 100])
plt.show()
