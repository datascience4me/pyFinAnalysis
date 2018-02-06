import quandl
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eur = pd.read_csv('eur_usd.csv')
print(eur['DateTime']).info()
# eur['DateTime'] = pd.to_datetime()
# #print(eur.tail())
#
# #eur.resample('60Min', how=sum, base=30)
# sample = eur.between_time(start_time = '21:00:00', end_time = '04:00:00', include_end = False)
#
# print(sample.tail())






