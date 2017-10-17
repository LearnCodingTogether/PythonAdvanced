import cv2
import numpy
#creating array from images 0 for gray image and 1 for bgr image
im_g=cv2.imread("smallgray.png",0)
print(im_g)

#creating images from numpy array
print(cv2.imwrite("newimage.png",im_g))

#to extract value from array
print(im_g[0:2,2:4])

#to transpose array
print(im_g.T)

#to trace each and every element of the array
for i in im_g.flat:
    print(i)

#STACKING
#horizontal stacking
ims=numpy.hstack((im_g,im_g))
print(ims)

#vertical stacking
ims1=numpy.vstack((im_g,im_g,im_g))
print(ims1)

#SPLITTING
#horizontal SPLITTING
ima=numpy.hsplit(ims,5)
print(ima)

#vertical SPLITTING
ima1=numpy.vsplit(ims,3)
print(ima1)
