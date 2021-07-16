import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from numpy import exp,arange

style.use('fivethirtyeight')

fig = plt.figure()
ax = fig.subplots()

x = []
y = []
def animate(i):
    x.append(i)
    y.append(((10**-15)*(exp(i/0.026)-1)))
    print(((10**-15)*(exp(i/0.026)-1)),i)
    ax.clear()
    ax.plot(x,y)

ani = animation.FuncAnimation(fig, animate, frames=arange(0,50,0.001),interval=0.1)
plt.show()