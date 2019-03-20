
# coding: utf-8

# In[3]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing(x):
    pass

def hsv_calc():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Trackbars",)
    cv2.createTrackbar("lh","Trackbars",0,179,nothing)
    cv2.createTrackbar("ls","Trackbars",0,255,nothing)
    cv2.createTrackbar("lv","Trackbars",0,255,nothing)
    cv2.createTrackbar("uh","Trackbars",179,179,nothing)
    cv2.createTrackbar("us","Trackbars",255,255,nothing)
    cv2.createTrackbar("uv","Trackbars",255,255,nothing)
    while True:
        ret, frame = cap.read()
        #frame = cv2.imread('candy.jpg')
        height, width = frame.shape[:2]
        #frame = cv2.resize(frame,(width/5, height/5), interpolation = cv2.INTER_CUBIC)
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        lh = cv2.getTrackbarPos("lh","Trackbars")
        ls = cv2.getTrackbarPos("ls","Trackbars")
        lv = cv2.getTrackbarPos("lv","Trackbars")
        uh = cv2.getTrackbarPos("uh","Trackbars")
        us = cv2.getTrackbarPos("us","Trackbars")
        uv = cv2.getTrackbarPos("uv","Trackbars")

        l_blue = np.array([lh,ls,lv])
        u_blue = np.array([uh,us,uv])
        mask = cv2.inRange(hsv, l_blue, u_blue)
        result = cv2.bitwise_or(frame,frame,mask=mask)

        #cv2.imshow("frame",frame)
        cv2.imshow("mask",mask)
        cv2.imshow("result",result)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

hsv_calc()

