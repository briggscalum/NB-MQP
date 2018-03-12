import numpy as np
import math
import matplotlib.pyplot as plt


def rotatepoint(xdata, ydata, angle):

	c, s = np.cos(angle), np.sin(angle)
	R = np.matrix('{} {}; {} {}'.format(c, -s, s, c))

	newxy = np.cross(R,np.array((xdata,ydata)))
	
	newxdata = -newxy[1]
	newydata = newxy[0]

	return newxdata, newydata




def rotateplot(xdata, ydata, angle):

	length = len(xdata)

	if(length != len(ydata)):
		print("Error: xdata and ydata are not of the same length. This is not a set of points.")
		return 0

	newxdata = [0] * length
	newydata = [0] * length

	c, s = np.cos(angle), np.sin(angle)
	R = np.matrix('{} {}; {} {}'.format(c, -s, s, c))

	for i in range (1, length): 
		
		newxy = np.cross(R,np.array((xdata[i],ydata[i])))
		
		newxdata[i] = -newxy[1]
		newydata[i] = newxy[0]

	return newxdata, newydata

def scaleplot(xdata, ydata, canvassize):

	maxx = max(xdata)
	minx = min(xdata)
	maxy = max(ydata)
	miny = min(ydata)

	wavex = [0] * len(xdata)
	wavey = [0] * len(ydata)

	
	#Scale Plot

	i = 0
	for xval in xdata:
		wavex[i] = ((xdata[i]) - (minx)) * (canvassize[0] /  (maxx-minx))
		i = i + 1
	i = 0
	for yval in ydata:
		wavey[i] = ((ydata[i]) - (miny)) * (canvassize[1] /  (maxy-miny)) 
		i = i + 1

	#Shift Plot

	wavex0 = wavex[0]
	wavey0 = wavey[0]
	
	i = 0
	for xval in wavex:
		wavex[i] = wavex[i] - wavex0
		i = i + 1
	i = 0
	for yval in wavey:
		wavey[i] = wavey[i] - wavey0
		i = i + 1




	return wavex, wavey


# Test Code
# wavex = [0] * 100;
# wavey = [0] * 100;

# for index in range (0,100):
# 	wavey[index] = math.sin(index/(100/(2*math.pi)))
# 	wavex[index] = float(index)

# wavex, wavey = rotateplot(wavex, wavey, math.pi)

# plt.plot(wavex,wavey)
# plt.show()


