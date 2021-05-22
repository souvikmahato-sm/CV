import numpy as np
from cv2 import cv2 as cv

def nothing(x) :
    print(x,end=' ')

img = np.zeros((512,512,3),np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('R','image',0,255,nothing)

while(1) :
    cv.imshow('image',img)
    key = cv.waitKey(1) & 0xFF
    if key ==27 :
        break
    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G','image')
    r = cv.getTrackbarPos('R','image')
    img[:] = [b,g,r]

cv.destroyAllWindows()