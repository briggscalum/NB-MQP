

pi = 3.141592
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

initialPos1 = [2, 0];
initialPos2 = [4, 0];

wavex = [0] * 10000
wavey = [0] * 10000
waveangle = [0] * 10000
distance1  = [0] * 10000
distance2  = [0] * 10000

# Angle between path point and grip point
pureangle1 = [0] * 10000
pureangle2 = [0] * 10000

# Adjusted Angle between path point and grip point to be written
angle1 = [0] * 10000
angle2 = [0] * 10000

path1x = [0] * 9999
path1y = [0] * 9999
path2x = [0] * 9999
path2y = [0] * 9999


# Generate line
for index in range (0,10000):
	wavey[index] = math.sin(index/(10000/(2*pi)))
	wavex[index] = index/(10000/(2*pi))

# Generate Instantanious Slopes
for index in range (0,9999):
	waveangle[index] = math.atan((wavey[index+1] - wavey[index]) / (wavex[index+1] - wavex[index]));


# Find Distance from path to hand
for index in range (0,9999):
	distance1[index] = math.sqrt((wavey[index] - initialPos1[1])**2 + (wavex[index] - initialPos1[0])**2);

for index in range (0,9999):
	distance2[index] = math.sqrt((wavey[index] - initialPos2[1])**2 + (wavex[index] - initialPos2[0])**2);


# Find angle from path to hand
for index in range (0,9999):
	pureangle1[index] = math.atan((wavey[index] - initialPos1[1]) / abs(wavex[index] - initialPos1[0]));
	if(wavex[index] - initialPos1[0] < 0): # adjustment based on arctan discontinuity
		pureangle1[index] = pi - pureangle1[index];

for index in range (0,9999):
	pureangle2[index] = math.atan((wavey[index] - initialPos2[1]) / abs(wavex[index] - initialPos2[0]));
	if(wavex[index] - initialPos2[0] < 0): # adjustment based on arctan discontinuity
		pureangle2[index] = pi - pureangle2[index];


# Find angle to write
for index in range (0,9999):
	angle1[index] = -(3*pi/4 - pureangle1[index] - waveangle[index]);

for index in range (0,9999):
	angle2[index] = -(3*pi/4 - pureangle2[index] - waveangle[index]);


# Create Path 1
for index in range (0,9999):
	path1x[index] = distance1[index]*math.cos(angle1[index]);
	path1y[index] = distance1[index]*math.sin(angle1[index]);

# Create Path 2
for index in range (0,9999):
	path2x[index] = distance2[index]*math.cos(angle2[index]);
	path2y[index] = distance2[index]*math.sin(angle2[index]);

# Create Drawn Path

sewpathx  = [0] * 10000
sewpathy  = [0] * 10000
ratio = 0;
minidistx = 0;
minidisty = 0;

for index in range (0,9999):
   	sewpathx[index]= math.hypot(wavex[index] - wavex[index-1], wavey[index]- wavey[index-1]);
	sewpathy[index]= 0;
	for j in range (1, index): 
		ratio = math.hypot(path1x[j], path1y[j]) / math.hypot(sewpathx[j], sewpathy[j])
		minidistx = path1x[j] - path1x[j-1]
		minidisty = path1y[j] - path1y[j-1]
		sewpathx[j] = sewpathx[j] + minidistx * ratio + math.hypot(wavex[index] - wavex[index-1], wavey[index]- wavey[index-1]);
		sewpathy[j] = sewpathy[j] + minidisty * ratio
	
#plot

fig = plt.figure()
#ax = plt.axes(xlim=(-3, 11), ylim=(-6, 6))
#line, = ax.plot([], [], lw=2)

plt.plot(initialPos1[0],initialPos1[1]);
plt.plot(initialPos2[0],initialPos2[1]);
plt.plot(path1x,path1y);
plt.plot(path2x,path2y);
plt.plot(sewpathx,sewpathy);


offsetwavex = [x+3 for x in wavex]
plt.plot(offsetwavex, wavey)
plt.show()

