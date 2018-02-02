import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

myYear = 2017
myMonth = 1
myDay = 2
myHour = 13
myMinute = 30
mySeconds = 15

myDate = datetime(myYear,myMonth,myDay,myHour,myMinute,mySeconds)
# print(myDate)
# print(type(myDate))     # this is important!

firstTwo = [datetime(2016,1,1), datetime(2016,1,2)]
print(firstTwo)
dtInd = pd.DatetimeIndex(firstTwo)      # creating date-time index!
print(dtInd)
data = np.random.randn(2,2)

df = pd.DataFrame(data, dtInd, columns=('a', 'b'))
print(df)




