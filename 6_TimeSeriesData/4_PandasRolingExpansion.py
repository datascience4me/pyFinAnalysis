import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('walmart_stock.csv', index_col='Date', parse_dates= True)

# rolling mean = Moving Average
# df['Open'].plot(figsize = (16,6))
#plt.show()

#print(df.rolling(10).mean().head(20))   # rolling(10) = MA (10)

# df['Open'].plot(c = 'blue')
# df.rolling(window=50).mean()['Close'].plot()     # open vs MA(7)

#adding a legend:
# df['Close 50 day MA'] = df['Close'].rolling(50).mean()
# df[['Close 50 day MA', 'Close']].plot()


# everything from the beginning of time series -> expanding
#df["Close"].expanding().mean().plot()

# Bollinger Bands:

# Close MA (20)
df['Close MA 20'] = df['Close'].rolling(20).mean()

# Upper band and lower band
df['Upper'] = df['Close MA 20'] + 2*(df['Close'].rolling(20).std())
df['Lower'] = df['Close MA 20'] - 2*(df['Close'].rolling(20).std())

# close prices
df[['Close', 'Close MA 20', 'Upper', 'Lower']].plot(figsize = (16,6))

plt.show()







