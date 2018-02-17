import cv2
import numpy as np
import matplotlib.pyplot as plt

def convert_grayscale(img_in):
	
	gray_image = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
	return gray_image

def threshold_image(img_in):
	ret,thresh = cv2.threshold(img_in,150,255,cv2.THRESH_BINARY)
	return thresh

def get_pixels(img_in):
	
	indices = np.where(img_in>[150])
	# print(np.shape(ices))
	a,b=(np.shape(indices))
	y=b-indices[0]
	
	x=indices[1]
	
	

# 
	# plt.plot(x,y)
	# plt.show()

	return x,y
	# polynomial=np.polyfit(x,y,3)
	# return polynomial
	
# 
def skeleton(img):
	row,col=np.shape(img)
	array=np.sum(img,axis=1).tolist()
	for f in range(0,len(array)):
		array[f]=array[f]/255
	print(array)

	for i in range(0,row):
		for j in range(0,col):
			if img[i,j]==255:
				img[i,:]=0
				num=int(j+array[i])
				print(num)
				img[i,num]=255
				break
	cv2.imshow('averaging',img)	
	
	cv2.waitKey(0)	
	return img


def skeletonization(img):
	size = np.size(img)
	skel = np.zeros(img.shape,np.uint8)
	 
	ret,img = cv2.threshold(img,127,255,0)
	element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
	done = False
	 
	while( not done):
	    eroded = cv2.erode(img,element)
	    temp = cv2.dilate(eroded,element)
	    temp = cv2.subtract(img,temp)
	    skel = cv2.bitwise_or(skel,temp)
	    img = eroded.copy()
	 
	    zeros = size - cv2.countNonZero(img)
	    if zeros==size:
	        done = True
	 
	cv2.imshow("skel",skel)
	cv2.waitKey(0)
	return skel
	
	# cv2.destroyAllWindows()




def load_and_show(img_in):
	# img_in="sinecurve3.png"
	image=cv2.imread(img_in,0)
	cv2.imshow('original_image',image)
	cv2.waitKey(0)
	binary_image=threshold_image(image)
	cv2.bitwise_not(binary_image,binary_image)
	cv2.imshow('binary',binary_image)
	cv2.waitKey(0)
	print(binary_image)
	print(np.shape(binary_image))
	# edges = cv2.Canny(binary_image,100,200)
	# plt.imshow(edges,cmap = 'gray')
	# plt.show()
	skel=skeletonization(binary_image)
	cv2.imshow('skeleton',skel)
	cv2.waitKey(0)
	# skel2=skeleton(skel)
	# blur = cv2.GaussianBlur(skel,(5,5),0)
	# cv2.imshow('smooth',blur)
	# cv2.waitKey(0)
	x,y=get_pixels(skel)
	return x,y



# if __name__ == "__main__":
# 	main()