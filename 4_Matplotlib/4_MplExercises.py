import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100)
y = x*2
z = x**2

def exc1():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 1, 1])
    ax.plot(x, y)
    ax.set_xlabel('X label')
    ax.set_ylabel('Y label')
    plt.show()

#exc1()

def exc2():
    fig = plt.figure()
    ax1 = fig.add_axes([0.1,0.1,1.1,1.1])
    ax2 = fig.add_axes([0.2,0.5,0.2,0.2])
    ax1.plot(x,y)
    ax2.plot(x,y, color = 'green')
    plt.show()

#exc2()

def exc3():
    fig = plt.figure()
    ax = fig.add_axes([0.1,0.1,1.1,1.1])
    ax = fig.add_axes([0.2,0.5,0.4,0.4])
    ax.plot(x,z)
    ax.set_xlabel('X')
    ax.set_ylabel('Z')






