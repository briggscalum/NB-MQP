"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

pi = 3.141592
Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=100000)
fig, ax = plt.subplots()

theta = np.radians(90)
c, s = np.cos(theta), np.sin(theta)
R = np.matrix('{} {}; {} {}'.format(c, -s, s, c))

wavex = [0] * 100
wavey = [0] * 100
waveangle = [0] * 100

frames = [[]]

distance = [0] * 100


# Generate line
for index in range (0,100):
	wavey[index] = math.sin(index/(100/(2*pi)))
	wavex[index] = index/(100/(2*pi))

# Generate Instantanious Distances
for index in range (1,100):
	distance[index] = math.hypot(wavex[index] - wavex[index-1], wavey[index]- wavey[index-1]);
	

# Generate Instantanious Slopes
for index in range (0,99):
	waveangle[index] = math.atan((wavey[index+1] - wavey[index]) / (wavex[index+1] - wavex[index]));


newxy = np.array([0, 0])
sewpathx = [0] * 100
sewpathy = [0] * 100
oldtheta = 0

for index in range (0,100):
	oldtheta = theta;
	theta = waveangle[index]
	c, s = np.cos(theta - oldtheta), np.sin(theta - oldtheta)
	R = np.matrix('{} {}; {} {}'.format(c, -s, s, c))
	#print R
   	for j in range (0, index+1): 
		newxy = np.cross(R,np.array((sewpathx[j],sewpathy[j] + distance[index])))
		sewpathx[j] = -newxy[1]
		sewpathy[j] = newxy[0]
	frames.append(plt.Line2D(sewpathx[0:index],sewpathy[0:index]));


line = plt.Line2D([0,0],[0,0], color = 'm')
line.set_data(frames[35].get_data())

ax.set_xlim([-5,5])
ax.set_ylim([-5,5])

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(frames[i].get_ydata())  # update the data
    line.set_xdata(frames[i].get_xdata())  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(4, 100), init_func=init,
                              interval=100, blit=True)

ani = animation.FuncAnimation(fig, animate, np.arange(4, 100), init_func=init,
                              interval=100, blit=True)

#ani.save('SewPath.mp4', writer=writer)
plt.show()
