def scaleplot(xdata, ydata, canvassize):

	maxx = max(xdata)
	minx = min(xdata)
	maxy = max(ydata)
	miny = min(ydata)

	wavex = [0] * len(xdata)
	wavey = [0] * len(ydata)

	i = 0
	for xval in xdata:
		wavex[i] = ((xdata[i]) - (minx)) * (canvassize[0] /  (maxx-minx)) - canvassize[0]/2 
		i = i + 1


	i = 0
	for yval in ydata:
		wavey[i] = ((ydata[i]) - (miny)) * (canvassize[1] /  (maxy-miny)) 
		i = i + 1

	return wavex, wavey