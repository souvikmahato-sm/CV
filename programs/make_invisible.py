from cv2 import cv2
import numpy as np

cap = cv2.VideoCapture("../samples/main1.mp4") ## your video
if cap.isOpened() == False :
    print("error")
ret = True
while(cap.isOpened()):
    ret ,  img = cap.read()
    if ret is True :
        img=np.rot90(img)
        back = cv2.imread("../samples/main2.jpg") ## clean plate of the background
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        l_b = np.array([60,92,55])
        u_b = np.array([70,255,255])
        mask1 = cv2.inRange(hsv,l_b,u_b)
        l_b = np.array([150, 70, 80])
        u_b = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv,l_b,u_b)
        mask1 = mask1 + mask2
        mask3 = cv2.bitwise_not(mask1)
        res1 = cv2.bitwise_and(img,img,mask=mask3)
        cv2.add(res1,back,dst=res1,mask = mask1)        
        cv2.imshow('res1',res1)
    
        key = cv2.waitKey(10) & 0xFF
        if key == 27 :
          break
    else :
        break
cap.release()

cv2.destroyAllWindows()
