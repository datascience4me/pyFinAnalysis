import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2


def figColor():
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.set_xlabel('Xlabel')
    ax.set_ylabel('Y Label')
    ax.plot(x,y, color = 'green', lw =2, alpha = 0.5, ls = '-', marker ='o', markersize = 10,
            markerfacecolor = 'blue')    # lw = width; alpha = line transparency; ls = style
    ax.set_xlim([0,1])      #seting limits on the axes
    ax.set_ylim([0,2])
    ax.plot()
    plt.show()

figColor()















