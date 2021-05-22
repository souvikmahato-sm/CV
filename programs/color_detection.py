from cv2 import cv2
import numpy as np

def nothing(x) :
    print(x,end=' ')

cv2.namedWindow('tracking')
cv2.createTrackbar('LH','tracking',0,255,nothing)
cv2.createTrackbar('LS','tracking',0,255,nothing)
cv2.createTrackbar('LV','tracking',0,255,nothing)
cv2.createTrackbar('UH','tracking',255,255,nothing)
cv2.createTrackbar('US','tracking',255,255,nothing)
cv2.createTrackbar('UV','tracking',255,255,nothing)

while(1) :
    img = cv2.imread("../samples/smarties.png")
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('LH','tracking')
    ls = cv2.getTrackbarPos('LS','tracking')
    lv = cv2.getTrackbarPos('LV','tracking')

    uh = cv2.getTrackbarPos('UH','tracking')
    us = cv2.getTrackbarPos('US','tracking')
    uv = cv2.getTrackbarPos('UV','tracking')

    l_b = np.array([lh,ls,lv])
    u_b = np.array([uh,us,uv])
    mask = cv2.inRange(hsv,l_b,u_b)
    detect = cv2.bitwise_and( img , img , mask=mask )
    
    cv2.imshow('img',img)
    cv2.imshow('mask',mask)
    cv2.imshow('detect',detect)
    key = cv2.waitKey(1) & 0xFF
    if key == 27 :
        break

cv2.destroyAllWindows()
