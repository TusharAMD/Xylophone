################### Simple Detect #############

# import cv2
# def mousePoints(event,x,y,flags,params):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x,y)
#
# img = cv2.imread('Resources/cards.jpg')
# cv2.imshow("Original Image ", img)
# cv2.setMouseCallback("Original Image ", mousePoints)
# cv2.waitKey(0)


######### WARP PRESPECTIVE IMPLEMANTAION WITH MOUSE CLICKS ##################

import cv2
import numpy as np
from matplotlib import pyplot as plt

circles = np.zeros((4,2),np.int)
counter = 0

def mousePoints(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:

        circles[counter] = x,y
        counter = counter + 1
        print(circles)

cap = cv2.VideoCapture(0)

while(True):
    ret,img1 = cap.read()
    img=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("fra",img)
    #while True:
    if counter == 4:
        width, height = 640,480
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        imgOutput = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("Output Image ", imgOutput)

    
    for x in range (0,4):
        cv2.circle(img,(circles[x][0],circles[x][1]),3,(0,255,0),cv2.FILLED)
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    #ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    #ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    #ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    #ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
    #titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    #images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
    #for i in range(6):
    #    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    #    plt.title(titles[i])
    #    plt.xticks([]),plt.yticks([])
    
    #plt.show()
    
    hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([40,50,50])
    upper_blue = np.array([70,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(thresh1,thresh1, mask= mask)
    
    cv2.imshow("Original Image ", res)
    cv2.imshow("Original Image2 ", img1)
    cv2.imshow("Original Image3 ", thresh1)
    cv2.setMouseCallback("Original Image ", mousePoints)
    cv2.waitKey(1)


