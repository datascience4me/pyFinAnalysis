import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'], ['W','X','Y','Z']) # excel-like sheet
print(df)
print('=' * 40)
# each of columns is pd series!!
#print(df['W'])      # main way
#print('=' * 40)
#print(df[['Y', 'Z']])  #two columns!

# create new column:
df['new'] = df['W'] + df['Y']
#print(df)

# delete a column

df = df.drop('new', axis=1)  # must use axis (0 or 1); doesn't have in-place, but you can set it inplace = True!
#print(df)                    # inplace = False is pd way to prevent deleting data by accident

# selecting rows:
print(df.loc['A'])      # rows are series as well!
print(df.iloc[0])       # iloc = index location -> using indices to select rows!
print(df.iloc[0:2])
print(df.loc[['A','B'],['W', 'Y']]) #get me WA and YZ cells! (like a1 and b4 in excel)


