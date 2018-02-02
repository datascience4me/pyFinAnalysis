import datetime
import pandas_datareader.data as web

start = datetime.datetime(2016,10,1)
end = datetime.datetime(2017,1,1)

fb = web.DataReader('FB', 'yahoo', start, end)
print(fb.head())





