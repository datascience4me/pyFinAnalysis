import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import seaborn as sns

df3 = pd.read_csv('df3')
'''
Recreate this scatter plot of b vs a. Note the color and size of the points. Also note the figure size.
See if you can figure out how to stretch it in a similar fashion. Remeber back to your matplotlib lecture...**
'''
def ex1():
    df3.plot.scatter(x='a', y = 'b',c = 'red', s = 50, figsize = (12,3))
    plt.show()
#ex1()


def ex2():
    '''
    Create a histogram of the 'a' column.**
    '''
    df3['a'].plot.hist(bins=20)
    plt.show()
#ex2()

def ex3():

    plt.style.use('ggplot')
    df3['a'].plot.hist(bins=20)
    plt.show()
#ex3()


def ex4():
    '''
    ** Create a boxplot comparing the a and b columns.**
    '''
    df3[['a','b']].plot.box()
    plt.show()
#ex4()

def ex5():
    '''
    ** Create a kde of d
    '''
    df3['d'].plot.kde(lw = 5, ls ='--')
    plt.show()
#ex5()

def ex6():
    '''
    ** Create an area plot of all the columns for just the rows up to 30. (hint: use .ix).**
    '''
    df3.ix[0:30].plot.area()        # .ix -> use this for slicing!!!
    plt.show()
#ex6()

def bonus():
    '''
    display the legend outside of the plot as shown below?**
    '''
    fig = plt.figure()
    df3.ix[0:30].plot.area(alpha = 0.4)
    plt.legend(loc = 'center left', bbox_to_anchor = (1.0, 0.5))
    plt.show()

bonus()
