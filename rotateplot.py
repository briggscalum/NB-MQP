import numpy as np
import math
import matplotlib.pyplot as plt

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


# Test Code
wavex = [0] * 100;
wavey = [0] * 100;

for index in range (0,100):
	wavey[index] = math.sin(index/(100/(2*math.pi)))
	wavex[index] = float(index)

wavex, wavey = rotateplot(wavex, wavey, math.pi)

plt.plot(wavex,wavey)
plt.show()


