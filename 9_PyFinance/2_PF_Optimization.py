import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

aapl = pd.read_csv('AAPL_CLOSE', index_col='Date', parse_dates=True)
cisco = pd.read_csv('CISCO_CLOSE', index_col='Date', parse_dates=True)
ibm = pd.read_csv('IBM_CLOSE', index_col='Date', parse_dates=True)
amzn = pd.read_csv('AMZN_CLOSE', index_col='Date', parse_dates=True)

stocks = pd.concat([aapl,cisco,ibm,amzn],axis=1)
stocks.columns = ['aapl', 'cisco', 'ibm', 'amzn']

# print(stocks.pct_change(1).mean())      # avg daily return
# print(stocks.pct_change(1).corr())      # correlation between daily returns

# Log returns
log_ret = np.log(stocks/stocks.shift(1))
# print(log_ret.cov()*252)

# Setting weights
np.random.seed(101)
weights = np.array(np.random.random(4))
# print('Random Weights')
# print(weights)

# REPEATING (PART 2)
num_ports = 1000
all_weights = np.zeros((num_ports,len(stocks.columns)))
ret_arr = np.zeros(num_ports)
vol_arr = np.zeros(num_ports)
sharpe_arr = np.zeros(num_ports)

for ind in r

# print('Rebalance')
weights = weights/np.sum(weights)
# print(weights)

# Expected Portfolio Return
exp_ret = np.sum((log_ret.mean()*weights)*252)

# Expected Variance (volatility)
exp_vol = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*252, weights)))   # complex look, but more code efficient

# Sharpe Ratio
# print('=' * 40)
# print(' Sharpe Ratio')

sr = exp_ret/exp_vol
# print(sr)

# PART 2







