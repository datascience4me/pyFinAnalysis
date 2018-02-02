import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# get data:
df1 = pd.read_csv('df1', index_col=0)
#print(df1.head())
df2 = pd.read_csv('df2')

# plot data
#df1.hist(['A'], bins = 30)
#df1.plot.hist(['A'])
#df2.plot.area()
#df2.plot.bar(stacked=True)
#df1.plot.line(x=df1.index,y='B',figsize=(12,3))
#df1.plot.scatter(x='A', y = 'B', c ='C',cmap = 'coolwarm') #by color
#df1.plot.scatter(x='A', y = 'B', s = df1['C']*100)  #by size
#df2.plot.box()
#df2.plot.density()
#plt.show()

# get 2-dimension data:
df = pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])

# plot data:
df.plot.hexbin(x='a',y='b', gridsize=25)                # for 2d fata frames
#plt.show()
