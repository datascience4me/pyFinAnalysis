import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import seaborn as sns

# get data:
mcd = pd.read_csv('mcdonalds.csv', index_col='Date', parse_dates=True)  #parse dates make datetime objects!
#print(mcd.head())

# dealing with different scales:
#mcd['Adj. Close'].plot()
#mcd['Adj. Volume'].plot()

#mcd['Adj. Close'].plot(xlim=['2007-01-01', '2009-01-01'],ylim = (20,50))   # setting data range
idx = mcd.loc['2007-01-01':'2007-05-01'].index
stock = mcd.loc['2007-01-01':'2007-05-01']['Adj. Close']
fig,ax = plt.subplots()
ax.plot_date(idx,stock, '-')
fig.autofmt_xdate()     # auto format x axis (dates)

# adding grid:
ax.yaxis.grid(True)
ax.xaxis.grid(True)

# LOCATING
ax.xaxis.set_major_locator(dates.MonthLocator())        #set ticks at every month (or weeks, days...)
ax.xaxis.set_major_formatter(dates.DateFormatter('\n\n%B--%y')) # capital B changes it to full month name, play with dashes, capital letters; \n->new line
ax.xaxis.set_minor_locator(dates.WeekdayLocator(byweekday=0)) #byweekday 0-> tuesday!!!
ax.xaxis.set_minor_formatter(dates.DateFormatter('%d'))     # adding another axis formatter!

plt.show()












