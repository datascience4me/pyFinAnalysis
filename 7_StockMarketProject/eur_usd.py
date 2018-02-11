import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eur = pd.read_csv('eur_usd.csv' , index_col='DateTime', parse_dates= True)
index_21_09 = pd.period_range('21:00:00', periods=9, freq='h')


#print(eur_period)
#eur.resample('120T', closed = 'right').ohlc()      #pokusao sam razne varijante ovde, ali rez mi je uvek isti cini mi se!!!
#eur.groupby(eur.index.minute).mean()
#print(eur.info())

index_21_09 = eur.index.indexer_between_time('21:00','05:00')   # Jovan
#index_21_09 = pd.period_range('21:00:00', periods=9, freq='h')  # ja

df = eur.iloc[index_21_09]


df_day_max = df.groupby(pd.Grouper(freq='8h', base = 5)).max()
df_day_min = df.groupby(pd.Grouper(freq = '8h', base = 5)).min()
df_group = (pd.concat([df_day_max['High'], df_day_min['Low ']], axis=1).dropna())

print(df_group.tail(30))
df_resample = df.resample('8H', base = 5).ohlc()
#print(df_resample.dropna())


# print(eur.head())
# print('=' * 50)
# print(res_eur.head())








