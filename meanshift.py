import cv2
import numpy as np
import sys
import cv

def choose(x):
	return {
	's':1,
	'r':2,
	'b':3,
	}[x]

def create_new(img):
	height, width, channels = img.shape
	return np.zeros((height,width,3),np.uint8)

def meanshift_segment(img,sp,sr,option):
	src = img
	i=0
	if(option == 's'):	
		while(i<=sp):
			dest = create_new(src)
			cv2.pyrMeanShiftFiltering(src,i,sr,dest)
			cv2.imwrite('filtered'+str(i)+'.jpeg',dest)
			src = dest
			i=i+10
	elif(option == 'r'):
		while(i<=sr):
			dest = create_new(src)
			cv2.pyrMeanShiftFiltering(src,sp,i,dest)
			cv2.imwrite('filtered'+str(i)+'.jpeg',dest)
			src = dest
			i=i+10
	elif(option == 'b'):
		i=0
		j=0
		k=0
		while(i<=sp and j<=sr):
			dest=create_new(src)
			cv2.pyrMeanShiftFiltering(src,i,j,dest)
			cv2.imwrite('filtered'+str(k)+'.jpeg',dest)
			src=dest
			i=i+10
			j=j+10
			k=k+1
			

def main():
	img = cv2.imread(sys.argv[1])
	sp = int(sys.argv[2])
	sr = int(sys.argv[3])
	option = sys.argv[4]
	meanshift_segment(img,sp,sr,option)
		
main()	
