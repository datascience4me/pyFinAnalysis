import quandl
quandl.ApiConfig.api_key = 'B_Ze7XHBmnx9Te_geMrd'           # enter api key here

#my_data = quandl.get('EIA/PET_RWTC_D')
#aapl = quandl.get('WIKI/AAPL')
#aapl = quandl.get('WIKI/AAPL.1')        # will return open column only
aapl = quandl.get('WIKI/AAPL', start_date = '2017-01-01', end_date = '2018-01-01')  # specific date range
#print(my_data.head())
print(aapl.head())

