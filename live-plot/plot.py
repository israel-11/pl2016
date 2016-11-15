import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
range = {
            'start' : -10,
            'end' : 10
        }
####################################################################
#                     LIVE PLOTTER                                 #
####################################################################
def animate(i):
    data = open("pl.txt","r").read()
    if len(data) > 0:
        if data != 'close' or data != 'stop':
            x = np.arange(range['start'], range['end'], 0.1)
            y = eval(data)
            ax1.clear()
            ax1.plot(x,y)
        else:
            plt.close()

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()