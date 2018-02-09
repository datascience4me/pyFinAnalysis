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

# Create Normalized (Cumulative) return:
for stock_df in (aapl,csco,ibm,amzn):
    stock_df['Norm Return'] = stock_df['Adj. Close']/stock_df.iloc[0]['Adj. Close']

# Create portfolio allocations:
for stock_df, allo in zip((aapl,csco,ibm,amzn),[0.3,0.2,0.4,0.1]):
    stock_df['Allocation'] = stock_df['Norm Return'] * allo

# Invested Values ($1.000.000)
for stock_df in (aapl,csco,ibm,amzn):
    stock_df['Position Value'] = stock_df['Allocation'] * 1000000

all_pos_vals = [aapl['Position Value'], csco['Position Value'], ibm['Position Value'],amzn['Position Value']]
portfolio_val = pd.concat(all_pos_vals, axis=1)
portfolio_val.columns = ['AAPL Pos', 'CSCO Pos','IBM Pos', 'AMZN Pos']
portfolio_val['Total Pos'] = portfolio_val.sum(axis = 1)
# portfolio_val['Total Pos'].plot()
# portfolio_val.drop('Total Pos', axis =1).plot()
#
# plt.show()


# PART 2

# Portfolio Stats
portfolio_val['Daily Return'] = portfolio_val['Total Pos'].pct_change(1)
portfolio_val['Daily Return'].mean()
portfolio_val['Daily Return'].std()
portfolio_val['Daily Return'].plot(kind = 'hist', bins = 100)
cumulative_return = 100* (portfolio_val['Total Pos'][-1]/portfolio_val['Total Pos'][0]-1)   # total return

# Sharpe Ratio
sr = portfolio_val['Daily Return'].mean()/portfolio_val['Daily Return'].std
sr = sr * (252**0.5)        # annualize = sqrt of 252
















