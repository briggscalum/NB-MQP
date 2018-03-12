import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
from changeplot import scaleplot, rotateplot, rotatepoint
from math import cos, sin
import vision


Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=100000)
fig, ax = plt.subplots()

theta = np.radians(-90)
c, s = np.cos(theta), np.sin(theta)
R = np.matrix('{} {}; {} {}'.format(c, -s, s, c))

frames = [[]]
frames2 = [[]]
frames3 = [[]]
frames4 = [[]]

canvassize = [0.2,0.3]

hand2pos = [0.1,0.0]
hand1pos = [0.2, 0.0]


#calculate intital distance and angle
intialdist1 =  math.hypot(hand1pos[1], canvassize[0]/2 -hand1pos[0])
intialdist2 =  math.hypot(hand2pos[1], canvassize[0]/2 -hand2pos[0])

intialangle1 =	np.arctan2(( canvassize[0]/2 -hand1pos[0]) , (hand1pos[1]));
intialangle2 =  np.arctan2(( canvassize[0]/2 -hand2pos[0]) , (hand2pos[1]));


# Generate line
# curve_name = 'sinecurve3.png'
# wavex,wavey = vision.load_and_show(curve_name)
# wavex = np.asfarray(wavex)
# wavey = np.asfarray(wavey)


wavex = [0] * 500;
wavey = [0] * 500;

for index in range (0,500):
	wavey[index] = math.sin(index/(500/(2*math.pi)))
	wavex[index] = float(index)

wavex, wavey = scaleplot(wavex,wavey,canvassize)


plt.plot(wavex,wavey);
ax.plot(hand1pos[0],hand1pos[1], marker='o', markersize=3, color="red")
ax.plot(hand2pos[0],hand2pos[1], marker='o', markersize=3, color="green")


length=(len(wavex))

# wavex=np.flip(wavex,0)
# wavey=np.flip(wavey,0)
# wavex=wavex[0:length-1:1]
# wavey=wavey[0:length-1:1]

length=len(wavey)
waveangle = [0] * length

# Angle between path point and grip point
pureangle1 = [0] * length
pureangle2 = [0] * length

# Adjusted Angle between path point and grip point to be written
angle1 = [0] * length
angle2 = [0] * length
distance = [0] * length

# Generate Instantanious Slopes
for index in range (0,length-1):
	waveangle[index] = np.arctan2((wavex[index+1] - wavex[index]) , (wavey[index+1] - wavey[index]));

# Generate Instantanious Distances
for index in range (1,length):
	distance[index] = math.hypot(wavex[index] - wavex[index-1], wavey[index]- wavey[index-1]);

# Create Drawn Path
sewpathx  = [0] * length
sewpathy  = [0] * length
hand1pathx = [0] * length
hand1pathy = [0] * length
hand2pathx = [0] * length
hand2pathy = [0] * length
hand1dist = math.sqrt(hand1pos[0]**2 + hand1pos[1]**2)
hand2dist = math.sqrt(hand2pos[0]**2 + hand2pos[1]**2)

#hand1pos[0] = hand1dist * cos(waveangle[0] - np.arctan2((wavex[0] - hand1pos[0]) , (wavey[0] - hand1pos[1])));
#hand1pos[1] = hand1dist * sin(waveangle[0] - np.arctan2((wavex[0] - hand1pos[0]) , (wavey[0] - hand1pos[1])));
 
hand1pos[0], hand1pos[1] = rotatepoint(hand1pos[0], hand1pos[1], 2*math.pi/3 - waveangle[0])
hand2pos[0], hand2pos[1] = rotatepoint(hand2pos[0], hand2pos[1], 2*math.pi/3 - waveangle[0])

# hand2pos[0] = hand2dist * cos(waveangle[0] - np.arctan2((wavex[0] - hand2pos[0]) , (wavey[0] - hand2pos[1])));
# hand2pos[1] = hand2dist * sin(waveangle[0] - np.arctan2((wavex[0] - hand2pos[0]) , (wavey[0] - hand2pos[1])));

newhand1path = {0.0,0.0}
newhand2path = {0.0,0.0}


for index in range (0,length):
	oldtheta = theta;
	theta = waveangle[index]
	c, s = np.cos(theta - oldtheta), np.sin(theta - oldtheta)
	R = np.matrix('{} {}; {} {}'.format(c, -s, s, c))
	
	if (index > 0):
		newhand1path = np.cross(R,np.array((hand1pathx[index-1],hand1pathy[index-1] + distance[index])))
		newhand2path = np.cross(R,np.array((hand2pathx[index-1],hand2pathy[index-1] + distance[index])))
	else:
		newhand1path = np.cross(R,np.array((hand1pos[0],hand1pos[1])))
		newhand2path = np.cross(R,np.array((hand2pos[0],hand2pos[1])))

	hand1pathx[index] = -newhand1path[1];
	hand1pathy[index] = newhand1path[0];

	hand2pathx[index] = -newhand2path[1];
	hand2pathy[index] = newhand2path[0];

	sewpathx, sewpathy = rotateplot(sewpathx, sewpathy, theta - oldtheta)

	for j in range (0, index): 
		sewpathy[j] = sewpathy[j] + distance[index]
		
	frames.append(plt.Line2D(sewpathx[1:index],sewpathy[1:index]))
	frames2.append(plt.Line2D(hand1pathx[1:index],hand1pathy[1:index]))
	frames3.append(plt.Line2D(hand2pathx[1:index],hand2pathy[1:index]))
	#frames4.append(ax.plot(hand1pathx[0:index], hand1pathy[0:index], 'o'))

	#frames2.append(plt.Line2D([sewpathx[0]+intialdist1*math.cos(waveangle[index] + intialangle1 - math.pi/4) , 0.7], [sewpathy[0]+intialdist1*math.sin(waveangle[index] + intialangle1 - math.pi/4) , 0]));
	#frames3.append(plt.Line2D([sewpathx[0]+intialdist2*math.cos(waveangle[index] + intialangle2 - math.pi/4) , -0.7],[sewpathy[0]+intialdist2*math.sin(waveangle[index] + intialangle2 - math.pi/4) , 0]));

# line = plt.Line2D([0,0],[0,0], color = 'm')
# line.set_data(frames[35].get_data())

ax.axis('equal')
ax.set_xlim([-0.5,0.5])
ax.set_ylim([-0.5,0.5])


x = np.arange(0, 2*np.pi, 2*np.pi/length)
line, = ax.plot(0, 0)
line2,  = ax.plot(0, 0)
line3,  = ax.plot(0, 0)
point, = ax.plot(0,0, 'o')

def animate(i):
	line.set_data(frames[i].get_data())  # update the data
	line2.set_data(frames2[i].get_data())  # update the data
	line3.set_data(frames3[i].get_data())  # update the data
	#graph.set_data(frames4[i].get_data())
	return line,line2,line3,point,


# Init only required for blitting to give a clean slate.
def init():
	line.set_ydata(np.ma.array(x, mask=True))
	return line,line2,line3,

ani = animation.FuncAnimation(fig, animate, np.arange(1, length), init_func=init,interval=50, blit=True)

#ani.save('SewPath.mp4', writer=writer)




plt.show()



