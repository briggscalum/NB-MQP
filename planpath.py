import matplotlib.pyplot as plt
import math

initialPos1 = [1.5, 0];
initialPos2 = [5, -2];

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
    wavey[index] = math.sin(index/(10000/(2*3.14159265)))
    wavex[index] = index/(10000/(2*3.14159265))

plt.plot(wavex, wavey)
plt.show()
