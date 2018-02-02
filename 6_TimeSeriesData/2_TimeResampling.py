import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('walmart_stock.csv')
df = pd.read_csv('walmart_stock.csv', index_col='Date', parse_dates= True)  # index_col = give a name to index; parse_dates = convert to datetime
#df['Date'] = pd.to_datetime(df['Date'])     # another way converting to date time format
#df.resample(rule = 'MS')
#print(df)

# do resample on your own with functions
def first_day(entry):
    return entry[0]        # the first entry of whatever

# df.resample(rule='M').apply(first_day)
# print(df)
df['Close'].resample('A').mean().plot(kind = 'bar', figsize = (16,6))
plt.show()

# Use filtering to only grab 3:25 or 3:30

