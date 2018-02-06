import quandl
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

tsla = pd.read_csv('Tesla_Stock.csv')
ford = pd.read_csv('Ford_Stock.csv')
gm = pd.read_csv('GM_Stock.csv')

# Create new column Daily Percentage Change (returns) -> rt = (Pt/Pt-1) - 1

#tsla['Returns'] = tsla['Close']/tsla['Close'].shift(1)-1
tsla['Returns'] = tsla['Close'].pct_change(1)   #pandas way (n) -> period
ford['Returns'] = ford['Close'].pct_change(1)
gm['Returns'] = gm['Close'].pct_change(1)
#print(tsla.head())

# Plot histogram of returns and judge volatility:
# tsla['Returns'].hist(bins = 100,label= 'Tesla', alpha = 0.5)
# ford['Returns'].hist(bins = 100, label= 'Ford', alpha = 0.5)
# gm['Returns'].hist(bins = 100, label='GM', alpha = 0.5)
# plt.legend()
# plt.show()

# KDE Plot
# tsla['Returns'].plot(kind = 'kde',label= 'Tesla')
# ford['Returns'].plot(kind = 'kde',label= 'Ford')
# gm['Returns'].plot(kind = 'kde',label= 'GM')
# plt.legend()
# plt.show()

# BOX PLOTS     (for this you need all the data in the same DF)

box_df = pd.concat([tsla['Returns'], ford['Returns'], gm['Returns']],axis=1)
box_df.columns = ['Tesla Ret', 'Ford Ret', 'GM Ret']
# box_df.plot(kind = 'box', figsize = (9,11))
# plt.show()

# Compare Daily returns between stocks -> scatter plot
#scatter_matrix(box_df, hist_kwds={'bins':100})
#plt.show()

# compare Ford and GM
# box_df.plot(kind = 'scatter', x = 'Ford Ret', y = 'GM Ret', alpha = 0.5)    # check with tesla also!
# plt.show()

# Cumulative Daily Returns (return over some period)
# Formula = (1+rt)it-1  use .cumprod() method!
tsla['Cum Return'] = (1+tsla['Returns']).cumprod()
ford['Cum Return'] = (1+ford['Returns']).cumprod()
gm['Cum Return'] = (1+gm['Returns']).cumprod()

#tsla['Cum Return'].plot(label = 'Tesla')
gm['Cum Return'].plot(label = 'GM')
ford['Cum Return'].plot(label = 'Ford')
plt.legend()
plt.show()



