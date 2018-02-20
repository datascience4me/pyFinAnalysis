import pandas as pd
import quandl
import matplotlib.pyplot as plt

quandl.ApiConfig.api_key = 'B_Ze7XHBmnx9Te_geMrd'

start = pd.to_datetime('2012-01-01')
end = pd.to_datetime('2017-01-01')

aapl = quandl.get('WIKI/AAPL', start_date = start, end_date = end)
csco = quandl.get('WIKI/CSCO', start_date = start, end_date = end)
ibm = quandl.get('WIKI/IBM', start_date = start, end_date = end)
amzn = quandl.get('WIKI/AMZN', start_date = start, end_date = end)

# print(aapl.iloc[0]['Adj. Close'])         # print rows with .iloc

# #Create Normalized (Cumulative) return:
for stock_df in (aapl,csco,ibm,amzn):
    stock_df['Norm Return'] = stock_df['Adj. Close']/stock_df.iloc[0]['Adj. Close']
# print(stock_df.head())


# Create portfolio allocations:
for stock_df, allo in zip((aapl,csco,ibm,amzn),[0.3,0.2,0.4,0.1]):
    stock_df['Allocation'] = stock_df['Norm Return'] * allo
# print(stock_df.head())

# # Invested Values ($1.000.000) => multiply allocations with deposits
for stock_df in (aapl,csco,ibm,amzn):
    stock_df['Position Value'] = stock_df['Allocation'] * 1000000
# print(aapl.head())

## Creating larger portfolio:
all_pos_vals = [aapl['Position Value'], csco['Position Value'], ibm['Position Value'],amzn['Position Value']]
portfolio_val = pd.concat(all_pos_vals, axis=1)       # concat previously made list
portfolio_val.columns = ['AAPL Pos', 'CSCO Pos','IBM Pos', 'AMZN Pos']
portfolio_val['Total Pos'] = portfolio_val.sum(axis = 1)  # create total positions by summing by axes = 1 -> rows
# print(portfolio_val.head())
portfolio_val['Total Pos'].plot()       # plotting portfolio value over time
portfolio_val.drop('Total Pos', axis =1).plot()   # check positions individually by dropping total pos column!

# plt.show()


# PART 2

# Portfolio Stats:

portfolio_val['Daily Return'] = portfolio_val['Total Pos'].pct_change(1)
# portfolio_val['Daily Return'].mean()  # get avg daily return column
# portfolio_val['Daily Return'].std()   # get st dev column
# portfolio_val['Daily Return'].plot(kind = 'hist', bins = 100)
# cumulative_return = 100 * (portfolio_val['Total Pos'][-1]/portfolio_val['Total Pos'][0]-1)   # total return by grabbing last and first


# # Sharpe Ratio:

# sr = portfolio_val['Daily Return'].mean()/portfolio_val['Daily Return'].std
# asr = sr * (252**0.5)        # annualized = sqrt of 252
















