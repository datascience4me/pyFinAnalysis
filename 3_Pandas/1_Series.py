'''
panel data; created for finance from the beginning
great for data frames; can read different formats (CSV, SQL...)
interacts great with matplotlib; it is very fast;
'''

# series are similar to arrays but you can give name to indices!
import numpy as np
import pandas as pd

# labels = ['a', 'b', 'c', 'd']
# my_list = [10,20,30]
# arr = np.array([10,20,30])
# d = {'a':10, 'b':20, 'c': 30}
#
# my_list = pd.Series(my_list)  # big S!
# print(my_list)
# #my_series_labels = pd.Series(my_list, index=labels)
# #print(my_series_labels)
# # you can use other data types also:
# my_series = pd.Series(arr)
# my_series_d = pd.Series(d)
# print(my_series,labels)
# print(my_series_d)
# print('=' * 40)
#
# #pd series can have diff data types
# my_series2 = pd.Series(data=labels)
# print(my_series2)

# using index with series
ser1 = pd.Series([1,2,3,4], index=['USA', 'CHINA','FRANCE', 'GERMANY'])
ser2 = pd.Series([1,2,3,4], index=['USA', 'CHINA','ITALY', 'GERMANY'])
print(ser1)
print('=' * 40)
print(ser2)
print(ser1['USA'])
print(ser2['ITALY'])
ser3 = ser1 + ser2
print(ser3)         #performs operations only when there is a match!!!





