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


######### WARP PRESPECTIVE ##################

import cv2
import numpy as np
import mediapipe as mp
from matplotlib import pyplot as plt
import pygame
from pygame import mixer
import time

circles = np.zeros((4,2),np.int)
counter = 0

def mousePoints(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:

        circles[counter] = x,y
        counter = counter + 1
        print(circles)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
flag=1
while(True):
    ret,img1 = cap.read()
    #img=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img=cv2.flip(img1, 1)
    #cv2.imshow("fra",img)
    #while True:
    if counter == 4:
        width, height = 640,480
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        imgOutput = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("For Hand ", imgOutput)
        if flag == 1:
            print(imgOutput.shape)
            flag=0
        image = cv2.cvtColor(cv2.flip(img1, 1), cv2.COLOR_BGR2RGB)
        #image = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        #imgOutput = cv2.cvtColor(cv2.flip(imgOutput, 1), cv2.COLOR_BGR2RGB)
        #imgOutput.flags.writeable = False
        results = hands.process(image)
        if results.multi_hand_landmarks:
            #print(len(results.multi_hand_landmarks))
            if len(results.multi_hand_landmarks)==1:
                for handLms in results.multi_hand_landmarks:
                    #print(handLms)
                    for id,lm in enumerate(handLms.landmark):
                        #h,w,c=img.shape()
                        h,w,c=image.shape
                        cx,cy=int(lm.x*w),int(lm.y*h)

                        adjcx=cx-circles[0][0]
                        adjcy=cy-circles[0][1]

                        #print(lm)
                        if id==8:
                            cv2.circle(image,(cx,cy),15,(255,0,255),cv2.FILLED)
                            #print(id,cx,cy)
                            print(id,adjcx,adjcy)

                            '''
                            For audio
                            '''
                            if adjcx<=18 and adjcx >=0 and adjcy<=300 and adjcy>=200:
                                mixer.init()
                                mixer.music.load("Notes/1.mp3")
                                mixer.music.play()
                                print("playing 1")
                                time.sleep(1)
                            elif adjcx<=38 and adjcx >=22 and adjcy<=300 and adjcy>=200:
                                mixer.init()
                                mixer.music.load("Notes/2.mp3")
                                mixer.music.play()
                                print("playing 2")
                                time.sleep(1)
                            elif adjcx<=55 and adjcx >=42 and adjcy<=300 and adjcy>=200:
                                mixer.init()
                                mixer.music.load("Notes/3.mp3")
                                mixer.music.play()
                                print("playing 3")
                                time.sleep(1)
                            elif adjcx<=87 and adjcx >=62 and adjcy<=300 and adjcy>=200:
                                mixer.init()
                                mixer.music.load("Notes/4.mp3")
                                mixer.music.play()
                                print("playing 4")
                                time.sleep(1)
                            elif adjcx<=103 and adjcx >=93 and adjcy<=300 and adjcy>=200:
                                mixer.init()
                                mixer.music.load("Notes/5.mp3")
                                mixer.music.play()
                                print("playing 5")
                                time.sleep(1)
                            elif adjcx<=130 and adjcx >=107 and adjcy<=300 and adjcy>=200:
                                mixer.init()
                                mixer.music.load("Notes/6.mp3")
                                mixer.music.play()
                                print("playing 6")
                                time.sleep(1)
                            elif adjcx<=150 and adjcx >=132 and adjcy<=300 and adjcy>=200:
                                mixer.init()
                                mixer.music.load("Notes/7.mp3")
                                mixer.music.play()
                                print("playing 7")
                                time.sleep(1)
                            elif adjcx<=170 and adjcx >=155 and adjcy<=300 and adjcy>=200:
                                mixer.init()
                                mixer.music.load("Notes/8.mp3")
                                mixer.music.play()
                                print("playing 8")
                                time.sleep(1)
                            elif adjcx<=195 and adjcx >=180 and adjcy<=300 and adjcy>=200:
                                mixer.init()
                                mixer.music.load("Notes/9.mp3")
                                mixer.music.play()
                                print("playing 9")
                                time.sleep(1)
                            elif adjcx<=210 and adjcx >=205 and adjcy<=300 and adjcy>=200:
                                mixer.init()
                                mixer.music.load("Notes/10.mp3")
                                mixer.music.play()
                                print("playing 10")
                                time.sleep(1)
                            elif adjcx<=238 and adjcx >=225 and adjcy<=300 and adjcy>=200:
                                mixer.init()
                                mixer.music.load("Notes/11.mp3")
                                mixer.music.play()
                                print("playing 11")
                                time.sleep(1)
                            elif adjcx<=255 and adjcx >=245 and adjcy<=300 and adjcy>=200:
                                mixer.init()
                                mixer.music.load("Notes/12.mp3")
                                mixer.music.play()
                                print("playing 12")
                                time.sleep(1)
                            elif adjcx<=282 and adjcx >=265 and adjcy<=300 and adjcy>=200:
                                mixer.init()
                                mixer.music.load("Notes/13.mp3")
                                mixer.music.play()
                                print("playing 13")
                                time.sleep(1)
                            elif adjcx<=305 and adjcx >=288 and adjcy<=300 and adjcy>=200:
                                mixer.init()
                                mixer.music.load("Notes/14.mp3")
                                mixer.music.play()
                                print("playing 14")
                                time.sleep(1)
                            elif adjcx<=333 and adjcx >=313 and adjcy<=300 and adjcy>=200:
                                mixer.init()
                                mixer.music.load("Notes/15.mp3")
                                mixer.music.play()
                                print("playing 15")
                                time.sleep(1)
                            ########Bottom one#########
                            elif adjcx<=18 and adjcx >=0 and adjcy<=30 and adjcy>=-20:
                                mixer.init()
                                mixer.music.load("Notes/16.mp3")
                                mixer.music.play()
                                print("playing 16")
                                time.sleep(1)
                            elif adjcx<=38 and adjcx >=22 and adjcy<=30 and adjcy>=-20:
                                mixer.init()
                                mixer.music.load("Notes/17.mp3")
                                mixer.music.play()
                                print("playing 17")
                                time.sleep(1)
                            elif adjcx<=55 and adjcx >=42 and adjcy<=30 and adjcy>=-20:
                                mixer.init()
                                mixer.music.load("Notes/18.mp3")
                                mixer.music.play()
                                print("playing 18")
                                time.sleep(1)
                            elif adjcx<=87 and adjcx >=62 and adjcy<=30 and adjcy>=-20:
                                mixer.init()
                                mixer.music.load("Notes/19.mp3")
                                mixer.music.play()
                                print("playing 19")
                                time.sleep(1)
                            elif adjcx<=115 and adjcx >=95 and adjcy<=30 and adjcy>=-20:
                                mixer.init()
                                mixer.music.load("Notes/20.mp3")
                                mixer.music.play()
                                print("playing 20")
                                time.sleep(1)
                            elif adjcx<=130 and adjcx >=117 and adjcy<=30 and adjcy>=-20:
                                mixer.init()
                                mixer.music.load("Notes/21.mp3")
                                mixer.music.play()
                                print("playing 21")
                                time.sleep(1)
                            elif adjcx<=153 and adjcx >=140 and adjcy<=30 and adjcy>=-20:
                                mixer.init()
                                mixer.music.load("Notes/22.mp3")
                                mixer.music.play()
                                print("playing 22")
                                time.sleep(1)
                            elif adjcx<=179 and adjcx >=163 and adjcy<=30 and adjcy>=-20:
                                mixer.init()
                                mixer.music.load("Notes/23.mp3")
                                mixer.music.play()
                                print("playing 23")
                                time.sleep(1)
                            elif adjcx<=200 and adjcx >=183 and adjcy<=30 and adjcy>=-20:
                                mixer.init()
                                mixer.music.load("Notes/24.mp3")
                                mixer.music.play()
                                print("playing 24")
                                time.sleep(1)
                            elif adjcx<=223 and adjcx >=207 and adjcy<=30 and adjcy>=-20:
                                mixer.init()
                                mixer.music.load("Notes/25.mp3")
                                mixer.music.play()
                                print("playing 25")
                                time.sleep(1)
                            elif adjcx<=240 and adjcx >=230 and adjcy<=30 and adjcy>=-20:
                                mixer.init()
                                mixer.music.load("Notes/26.mp3")
                                mixer.music.play()
                                print("playing 26")
                                time.sleep(1)
                            elif adjcx<=255 and adjcx >=245 and adjcy<=30 and adjcy>=-20:
                                mixer.init()
                                mixer.music.load("Notes/27.mp3")
                                mixer.music.play()
                                print("playing 27")
                                time.sleep(1)
                            elif adjcx<=276 and adjcx >=266 and adjcy<=30 and adjcy>=-20:
                                mixer.init()
                                mixer.music.load("Notes/28.mp3")
                                mixer.music.play()
                                print("playing 28")
                                time.sleep(1)
                            elif adjcx<=300 and adjcx >=285 and adjcy<=30 and adjcy>=-20:
                                mixer.init()
                                mixer.music.load("Notes/29.mp3")
                                mixer.music.play()
                                print("playing 29")
                                time.sleep(1)
                            elif adjcx<=327 and adjcx >=307 and adjcy<=30 and adjcy>=-20:
                                mixer.init()
                                mixer.music.load("Notes/30.mp3")
                                mixer.music.play()
                                print("playing 30")
                                time.sleep(1)
                    mpDraw.draw_landmarks(image,handLms,mpHands.HAND_CONNECTIONS)
            cv2.imshow("Output Image 2", image)

    
    for x in range (0,4):
        cv2.circle(img,(circles[x][0],circles[x][1]),3,(0,255,0),cv2.FILLED)
    ret,thresh1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
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

    cv2.putText(img,"Please select 4 vertices", (100,100),cv2.FONT_HERSHEY_SIMPLEX,1.3,(150,180,105),3)
    #cv2.imshow("Original Image ", res)
    if counter<4:
        cv2.imshow("Original Image2 ", img)
    
    #cv2.imshow("Original Image3 ", thresh1)
    cv2.setMouseCallback("Original Image2 ", mousePoints)
    cv2.waitKey(1)
    

