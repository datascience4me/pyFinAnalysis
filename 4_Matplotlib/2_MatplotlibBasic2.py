import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

def ooSubplots():
    # create subplots
    fig, axes = plt.subplots(nrows=1, ncols=2)
    axes.plot(x, y)
    plt.show()

#ooSubplots()

def figSize():
    fig = plt.figure(figsize=(8,2), dpi=100)    # 3 = width; dpi = pixels per inch
    ax = fig.add_axes([0,0,1,1])
    ax.plot(x,y)
    plt.show()
#figSize()

# saving figure:
# fig.savefig('name.filetype')

# adding legend
def legend():
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.plot(x, x**2, label = 'x squared')
    ax.plot(x,x**3, label = 'x cubed')
    ax.legend(loc = 10)       #loc = location by location string or code
    plt.show()

legend()














