import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('walmart_stock.csv', index_col='Date', parse_dates= True)  # daily data
print(df.head())
print('='*40)
#print(df.shift(periods=1).head())   # now you don't have any value (NaN) for the first row and all other data have been shifted!
# periods can be negative to do backward shifting!

print(df.tshift(freq='A').head())   # pay attention to index!




