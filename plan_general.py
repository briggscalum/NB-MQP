

pi = 3.141592
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
from math import cos, sin
import trial2


Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=100000)
fig, ax = plt.subplots()

theta = np.radians(90)
c, s = np.cos(theta), np.sin(theta)
R = np.matrix('{} {}; {} {}'.format(c, -s, s, c))


frames = [[]]
frames2 = [[]]
frames3 = [[]]

initialPos1 = [400, 0];
initialPos2 = [300, 0];




# Generate line


curve_name="sinecurve3.png"
wavex,wavey=trial2.load_and_show(curve_name)

# plt.plot(wavex,wavey)
# plt.show()
length=(len(wavex))


# print(wavey)
# print(wavex)
wavex=np.flip(wavex,0)
wavey=np.flip(wavey,0)
wavex=wavex[0:length-1:1]
wavey=wavey[0:length-1:1]
# plt.plot(wavex,wavey)
# plt.show()
print(wavex)
print(wavey)
# wavex = [0] * length
# wavey = [0] * length
length=len(wavey)
waveangle = [0] * length
# Angle between path point and grip point
pureangle1 = [0] * length
pureangle2 = [0] * length

# Adjusted Angle between path point and grip point to be written
angle1 = [0] * length
angle2 = [0] * length
distance = [0] * length
# Generate line
# for index in range (0,100):
# 	wavey[index] = math.cos(index/(100/(2*pi)))
# 	wavex[index] = index/(100/(2*pi))

# Generate Instantanious Slopes
for index in range (0,length-1):
	waveangle[index] = math.atan((wavey[index+1] - wavey[index]) / (wavex[index+1] - wavex[index]));

# Generate Instantanious Distances
for index in range (1,length):
	distance[index] = math.hypot(wavex[index] - wavex[index-1], wavey[index]- wavey[index-1]);

# Create Drawn Path
sewpathx  = [0] * length
sewpathy  = [0] * length
ratio = 0;
minidistx = 0;
minidisty = 0;

for index in range (0,length):
	oldtheta = theta;
	theta = waveangle[index]
	c, s = np.cos(theta - oldtheta), np.sin(theta - oldtheta)
	R = np.matrix('{} {}; {} {}'.format(c, -s, s, c))
	for j in range (0, index+1): 
		newxy = np.cross(R,np.array((sewpathx[j],sewpathy[j] + distance[index])))
		sewpathx[j] = -newxy[1]
		sewpathy[j] = newxy[0]
	frames.append(plt.Line2D(sewpathx[0:index],sewpathy[0:index]));
	frames2.append(plt.Line2D([sewpathx[0]+2*math.cos(waveangle[index] - pi/2) , 7],[sewpathy[0]+2*math.sin(waveangle[index] - pi/2) , 0]));
	frames3.append(plt.Line2D([sewpathx[0]+5*math.cos(waveangle[index] - pi/2) , -7],[sewpathy[0]+5*math.sin(waveangle[index] - pi/2) , 0]));

line = plt.Line2D([0,0],[0,0], color = 'm')
line.set_data(frames[35].get_data())

ax.set_xlim([-300,1000])
ax.set_ylim([-1000,4000])

x = np.arange(0, 2*np.pi, 2*np.pi/length)
line, = ax.plot(x, np.sin(x))
line2,  = ax.plot(x, np.sin(x))
line3,  = ax.plot(x, np.sin(x))

def animate(i):
	line.set_ydata(frames[i].get_ydata())  # update the data
	line.set_xdata(frames[i].get_xdata())  # update the data
	line2.set_ydata(frames2[i].get_ydata())  # update the data
	line2.set_xdata(frames2[i].get_xdata())  # update the data
	line3.set_ydata(frames3[i].get_ydata())  # update the data
	line3.set_xdata(frames3[i].get_xdata())  # update the data
	return line,line2,line3,


# Init only required for blitting to give a clean slate.
def init():
	line.set_ydata(np.ma.array(x, mask=True))
	return line,line2,line3,

ani = animation.FuncAnimation(fig, animate, np.arange(1, length), init_func=init,interval=150, blit=True)

#ani = animation.FuncAnimation(fig, animate, np.arange(4, 100), init_func=init, interval=50, blit=True)

#ani.save('SewPath.mp4', writer=writer)
plt.show()