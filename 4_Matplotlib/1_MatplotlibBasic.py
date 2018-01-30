import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

# FUNCTIONAL METHOD:
def funcMethod():
    plt.plot(x, y)
    plt.xlabel('X Label')
    plt.ylabel('Y label')
    plt.title('Title')
    plt.subplot(1,2,1)       #creating multiplots -> no of rows, columns and plot number you are refferring to
    plt.plot(x, y, 'r')
    plt.subplot(1,2,2)
    plt.plot(y,x, 'b')
    plt.show()
#funcMethod()

# OBJECT ORIENTED METHOD -> better way
def ooMethod():
    fig = plt.figure()      # empty canvas to be accessed!
    axes = fig.add_axes([0.1,0.1,0.8,0.8])  #left, bottom, width and height -> must be 0-1, think in %
    axes.plot(x,y)
    axes.set_xlabel('Xlabel')
    axes.set_ylabel('Y Label')
    plt.show()

#ooMethod()

def  ooMethod2():
    fig = plt.figure()
    axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
    axes2 = fig.add_axes([0.15,0.5,0.4,0.3])
    axes1.plot(x,y)
    axes2.plot(y,x)
    plt.show()

ooMethod2()
