"""import pandas 
soubor = pandas.read_csv('korelace.csv',error_bad_lines=False)
print(soubor)
soubor.iloc[:,0]
print(soubor.iloc[:,0])
soubor.iloc[:,2]
print(soubor.iloc[:,2])
rank = soubor.iloc[:,0]
owners = soubor.iloc[:,2]
rank.corr(owners)
print(rank.corr(owners))
import matplotlib.pyplot as plt
plt.style.use('ggplot')"""
import numpy as np
import scipy.stats
"""import pandas 
soubor = pandas.read_csv('korelace.csv',sep = ';',error_bad_lines=False)
rank = soubor.iloc[:,0]
owners = soubor.iloc[:,2]
slope, intercept, r, p, stderr = scipy.stats.linregress(rank,owners)
line = f'Regression line: rank={intercept:.2f}+{slope:.2f}owners, r={r:.2f}'
print(line)"""


