import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
how to get best portfolio, best sharpe ratio - which allocations???
you can guess and try all possible combinations, i.e. use monte carlo analysis
or you can optimize by using math -> use minimization  to create optimizer to minimize negative sharpe ratio
use scipy built in algorithm
'''

# PART 1 - Monte Carlo Simulation:

aapl = pd.read_csv('AAPL_CLOSE', index_col='Date', parse_dates=True)
cisco = pd.read_csv('CISCO_CLOSE', index_col='Date', parse_dates=True)
ibm = pd.read_csv('IBM_CLOSE', index_col='Date', parse_dates=True)
amzn = pd.read_csv('AMZN_CLOSE', index_col='Date', parse_dates=True)

stocks = pd.concat([aapl,cisco,ibm,amzn],axis=1)    # concatenate all csv files together in one df
stocks.columns = ['aapl', 'cisco', 'ibm', 'amzn']
# print(type(stocks))
# print(stocks.head())

# print(stocks.pct_change(1).mean())      # avg daily return
# print(stocks.pct_change(1).corr())      # correlation between daily returns

# # Log returns -> use it for de-trending (not arithmetic returns):

log_ret = np.log(stocks/stocks.shift(1))
# # print(log_ret.cov()*252)
# log_ret.hist(bins = 100)
# log_ret.cov()     # to get allocations
# plt.show()

# # Setting weights
np.random.seed(101)
# weights = np.array(np.random.random(4))
# print('Random Weights:')
# print(weights)
# print('Rebalanced Weights:')
# weights = weights/np.sum(weights)       # rebalance them so the sum of them is equal to 1!
# print(weights)
#
# # Expected Return/Variance
# exp_ret = np.sum((log_ret.mean()*weights)*252)
# print('Expected Return:')
# print(exp_ret)
# exp_vol = np.sqrt(np.dot(weights.T,np.dot(log_ret.cov()*252,weights)))
# print("Expected Volatility:")
# print(exp_vol)
#
# sr = exp_ret/exp_vol
# print('Sharpe Ratio:')
# print(sr)

# PART 2
'''
put previously made process into the for loop
'''
# Create variables to save results to be plotted later

num_ports = 100        # no of portfolios
all_weights = np.zeros((num_ports,len(stocks.columns)))
ret_arr = np.zeros(num_ports)   # array that holds returns
vol_arr = np.zeros(num_ports)   # array that holds vol.
sharpe_arr = np.zeros(num_ports)    # array of all possible pf SR

for ind in range(num_ports):
    np.random.seed(101)
    weights = np.array(np.random.random(4))
    weights = weights / np.sum(weights)

    # save weights:
    all_weights[ind,:] = weights

    # Exp return
    ret_arr = np.sum((log_ret.mean() * weights) * 252)

    # Exp vol
    vol_arr = np.sqrt(np.dot(weights.T,np.dot(log_ret.cov()*252,weights)))

    # Sharpe Ratio
    sharpe_arr[ind] = ret_arr[ind]/vol_arr[ind]      # dividing every exp ret with its exp vol using ind from for loop










