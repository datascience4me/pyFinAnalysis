import quandl
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# Getting the data:

tsla = pd.read_csv('Tesla_Stock.csv', index_col = 'Date', parse_dates = True)
ford = pd.read_csv('Ford_Stock.csv', index_col = 'Date', parse_dates = True)
gm = pd.read_csv('GM_Stock.csv', index_col = 'Date', parse_dates = True)
#print(tsla.head())

# Getting data from qunadl:

# import quandl
# quandl.ApiConfig.api_key = 'B_Ze7XHBmnx9Te_geMrd'
# gm = quandl.get('WIKI/GM', start_date = '2017-01-01', end_date = '2018-01-01')

# Plotting open price (unadjusted)
# tsla['Open'].plot(label = 'Tesla', title = 'Opening Prices')
# gm['Open'].plot(label = 'GM')
# ford['Open'].plot(label = 'Ford')
# plt.legend()
# plt.show()

# Plotting volume (unadjusted)
# tsla['Volume'].plot(label = 'Tesla', title = 'Volume Traded')
# gm['Volume'].plot(label = 'GM')
# ford['Volume'].plot(label = 'Ford')
# print(ford['Volume'].argmax())
# plt.legend()
# plt.show()

# # Total money traded -> Volume * Open price

# def tmt():
#     tsla['Total Traded'] = tsla['Open'] * tsla['Volume']    # this way you create new column!
#     ford['Total Traded'] = ford['Open'] * ford['Volume']
#     gm['Total Traded'] = gm['Open'] * gm['Volume']
#
#     tsla['Total Traded'].plot(label = 'Tesla')
#     ford['Total Traded'].plot(label = 'Ford')
#     gm['Total Traded'].plot(label = 'GM')
#     print(tsla.tail())
#     plt.legend()
#     plt.show()
# tmt()

# Plotting MA 50 and MA 200 for GM

# gm['Open'].plot(label = 'GM Open Price')
# gm_ma50 = gm['Open'].rolling(50).mean()      # or to this as a new column with gm['MA50']
# gm_ma50.plot(label ='MA 50')
# gm_ma200 = gm['Open'].rolling(200).mean()
# gm_ma200.plot(label = 'MA 200')
# plt.legend()
# plt.show()

# Correlations
'''
first you need to rearrange data into single DF using pd.concat (what and how(rows/columns) you want to concat)!
'''

# car_comp = pd.concat([tsla['Open'],gm['Open'], ford['Open']], axis=1)
# car_comp.columns = ['Tesla Open', 'GM Open', 'Ford Open']
# scatter_matrix(car_comp, figsize=(12,8), alpha = 0.2, hist_kwds={'bins': 50})   # add bins with key values in dict hist_kwds
# plt.show()
#print(car_comp.head())

# Candlestick Chart - Bonus

from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, date2num,WeekdayLocator, DayLocator, MONDAY
ford_reset = ford.loc['2012-01'].reset_index()      # grabbed all in Jan and reset index
ford_reset['date_ax'] = ford_reset['Date'].apply(lambda  date:date2num(date))   # creating numerical value for dates
list_of_columns = ['date_ax', 'Open', 'High', 'Low', 'Close']
ford_values = [tuple(vals) for vals in ford_reset[list_of_columns].values]
#print(ford_values)

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)

candlestick_ohlc(ax, ford_values, width=0.6, colorup='green', colordown='red')
plt.show()






