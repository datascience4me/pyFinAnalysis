# You can consider CAPM as simple linear regression!
from scipy import stats
import pandas_datareader as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start = pd.to_datetime('2010-01-04')
end = pd.to_datetime('2017-07-25')

spy_etf = web.DataReader('SPY', 'yahoo', start, end)
# print(spy_etf.info())
aapl = web.DataReader('AAPL', 'yahoo', start, end)
# aapl['Adj Close'].plot(label = 'AAPL')
# spy_etf['Adj Close'].plot(label = 'SPY')


# Compare Cumulative returns
aapl['Cumulative Returns'] = aapl['Close']/aapl['Close'].iloc[0]
spy_etf['Cumulative Returns'] = spy_etf['Close']/spy_etf['Close'].iloc[0]
# aapl['Cumulative Returns'].plot(label = 'AAPL Cumulative Return')
# spy_etf['Cumulative Returns'].plot(label = 'SPY Cumulative Return')

# Daily returns

aapl['Daily Returns'] = aapl['Close'].pct_change(1)
spy_etf['Daily Returns'] = spy_etf['Close'].pct_change(1)
# plt.scatter(aapl['Daily Returns'], spy_etf['Daily Returns'],alpha=0.25)

beta,alpha,r_value,p_value,std_err = stats.linregress(aapl['Daily Returns'].iloc[1:],
                                                      spy_etf['Daily Returns'].iloc[1:]) # you cant pass zeros that are in first row

# print(alpha, beta)

noise = np.random.normal(0,0.001, len(spy_etf['Daily Returns'].iloc[1:]))
fake_stock = spy_etf['Daily Returns'].iloc[1:] + noise
plt.scatter(fake_stock, spy_etf['Daily Returns'].iloc[1:],alpha=0.25)

beta,alpha,r_value,p_value,std_err = stats.linregress(fake_stock,
                                                      spy_etf['Daily Returns'].iloc[1:])
# NOW CHECK BETA/ALPHA VALUES!!
# print(alpha, beta)

# plt.legend()
plt.show()





