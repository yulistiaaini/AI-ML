from threading import Thread

import csv
import os,sys,time
import numpy as np
import cv2

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 

def seluruh1():
# init camera
    camera = cv2.VideoCapture('Video/rorisnyontek.mp4')   ### <<<=== SET THE CORRECT CAMERA NUMBER
    camera.set(3,1280)             # set frame width
    camera.set(4,720)              # set frame height
    time.sleep(0.5)
    print(camera.get(3),camera.get(4))

    # master frame
    x_value = 0
    total_1 = 0
    master = None

    fieldnames = ["x_value", "total_1"]
    jum=0
    total=0

    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        
    while 1:
        
        # grab a frame 10,400),(200,700
        (grabbed,frame) = camera.read()
      
        frame0 = cv2.resize(frame, (1280, 720)) 
        # end of feed
        if not grabbed:
            break

        # gray frame
        frame1 = cv2.cvtColor(frame0,cv2.COLOR_BGR2GRAY)

        # blur frame
        frame2 = cv2.GaussianBlur(frame1,(15,15),0)

        # initialize master
        if master is None:
            master = frame2
            continue

        # delta frame
        frame3 = cv2.absdiff(master,frame2)

        # threshold frame
        frame4 = cv2.threshold(frame3,15,255,cv2.THRESH_BINARY)[1]

        # dilate the thresholded image to fill in holes
        kernel = np.ones((2,2),np.uint8)
        frame5 = cv2.erode(frame4,kernel,iterations=4)
        frame5 = cv2.dilate(frame5,kernel,iterations=8)

        img1 = frame5[300:500,550:750]
        img1kepala = frame5[300:430,550:750]
        img1tangan = frame5[430:500,550:750]
        n_white_pix1 = np.sum(img1 == 255)
        n_white_pix1kepala = np.sum(img1tangan == 255)
        n_white_pix1tangan = np.sum(img1kepala == 255)

        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info = {
                "x_value": x_value,
                "total_1": total_1
            }

            csv_writer.writerow(info)
            print(x_value, total_1, jum, total)
                    
            x_value += 1
            total_1 = n_white_pix1


        # find contours on thresholded image
        nada,contours,nada = cv2.findContours(frame5.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        # make coutour frame
        frame6 = frame0.copy()

        cv2.rectangle(frame6,(550,300),(750,500),(0,255,0),2)

        if (n_white_pix1>506):
             cv2.rectangle(frame6,(550,300),(750,500),(0,0,255),2)
             
        cv2.putText(frame6,'Participant 1 : ' + str(total) + ' moves', 
                (550,290), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
                    
        # target contours
        targets = []

        # loop over the contours
        for c in contours:
            
            # if the contour is too small, ignore it
            if cv2.contourArea(c) < 230:
                    continue

            # contour data
            M = cv2.moments(c)#;print( M )
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            x,y,w,h = cv2.boundingRect(c)
            rx = x+int(w/2)
            ry = y+int(h/2)
            ca = cv2.contourArea(c)

            # plot contours
            cv2.drawContours(frame6,[c],0,(0,0,255),2)
            cv2.rectangle(frame6,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(frame6,(cx,cy),2,(0,0,255),2)
            cv2.circle(frame6,(rx,ry),2,(0,255,0),2)

            # save target contours
            targets.append((cx,cy,ca))

        
        # update master
        master = frame2

        img2 = frame6[250:550,350:800]

        # display
##        cv2.imshow("Frame0: Raw",frame0)
##        cv2.imshow("Frame1: Gray",frame1)
##        cv2.imshow("Frame2: Blur",frame2)
##        cv2.imshow("Frame3: Delta",frame3)
##        cv2.imshow("Frame4: Threshold",frame4)
##        cv2.imshow("Frame5: Dialated",frame5)
        cv2.imshow("Frame6: Contours",frame6)
      ##  cv2.imshow("Frame7: Crop",img1kepala)
         
        if (n_white_pix1 > 500):
            jum+=1
        elif (n_white_pix1 < 500):
            jum=0
        if (jum == 5):
            total+=1
        

        # key delay and action
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            break
        elif key != 255:
            print('key:',[chr(key)])

    # release camera
    camera.release()

        
    # close all windows
    cv2.destroyAllWindows()
    
def seluruh4():
    # init camera
    camera = cv2.VideoCapture('Video/Empatduabaris.mp4')   ### <<<=== SET THE CORRECT CAMERA NUMBER
    camera.set(3,1280)             # set frame width
    camera.set(4,720)              # set frame height
    time.sleep(0.5)
    print(camera.get(3),camera.get(4))

    # master frame
    x_value = 0
    total_1 = 0
    total_2 = 0
    total_3 = 0
    total_4 = 0
    master = None

    fieldnames = ["x_value", "total_1", "total_2", "total_3", "total_4"]
    waktu = [0,0,0]
    i=0

    jum1=0
    jum2=0
    jum3=0
    jum4=0

    total1=0
    total2=0
    total3=0
    total4=0

    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    while 1:
        # grab a frame 10,400),(200,700
        (grabbed,frame) = camera.read()

        frame0 = cv2.resize(frame,(1280, 720)) 
        # end of feed
        if not grabbed:
            break

        # gray frame
        frame1 = cv2.cvtColor(frame0,cv2.COLOR_BGR2GRAY)

        # blur frame
        frame2 = cv2.GaussianBlur(frame1,(15,15),0)

        # initialize master
        if master is None:
            master = frame2
            continue

        # delta frame
        frame3 = cv2.absdiff(master,frame2)

        # threshold frame
        frame4 = cv2.threshold(frame3,15,255,cv2.THRESH_BINARY)[1]

        # dilate the thresholded image to fill in holes
        kernel = np.ones((2,2),np.uint8)
        frame5 = cv2.erode(frame4,kernel,iterations=4)
        frame5 = cv2.dilate(frame5,kernel,iterations=8)
        
        img1 = frame5[150:330,430:630]
        img2 = frame5[150:330,780:980]
        img3 = frame5[370:550,400:600]
        img4 = frame5[370:550,980:1180]
        
        n_white_pix1 = np.sum(img1 == 255)
        n_white_pix2 = np.sum(img2 == 255)
        n_white_pix3 = np.sum(img3 == 255)
        n_white_pix4 = np.sum(img4 == 255)
        
        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info = {
                "x_value": x_value,
                "total_1": total_1,
                "total_2": total_2,
                "total_3": total_3,
                "total_4": total_4
            }
            
            csv_writer.writerow(info)
            print(x_value, total_1, total_2, total_3, total_4)
                    

            x_value += 1
            total_1 = n_white_pix1
            total_2 = n_white_pix2
            total_3 = n_white_pix3
            total_4 = n_white_pix4


        # find contours on thresholded image
        nada,contours,nada = cv2.findContours(frame5.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        # make coutour frame
        frame6 = frame0.copy()
        
        cv2.rectangle(frame6,(430,150),(630,330),(0,255,0),2)
        cv2.rectangle(frame6,(780,150),(980,330),(0,255,0),2)
        cv2.rectangle(frame6,(400,370),(600,550),(0,255,0),2)
        cv2.rectangle(frame6,(980,370),(1180,550),(0,255,0),2)

        cv2.putText(frame6,'Participant 1: '+ str(total1)+' moves', 
            (430,145), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)
        cv2.putText(frame6,'Participant 2: '+str(total2)+' moves', 
            (780,145), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)
        cv2.putText(frame6,'Participant 3: '+str(total3)+' moves', 
            (400,360), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)
        cv2.putText(frame6,'Participant 4: '+str(total4)+' moves', 
            (980,360), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)

        
        if (n_white_pix1>389):
            cv2.rectangle(frame6,(430,150),(630,330),(0,0,255),2)
        if (n_white_pix2>389):
            cv2.rectangle(frame6,(780,150),(980,330),(0,0,255),2)
        if (n_white_pix3>389):
            cv2.rectangle(frame6,(400,370),(600,550),(0,0,255),2)
        if (n_white_pix4>389):
            cv2.rectangle(frame6,(980,370),(1180,550),(0,0,255),2)

        # target contours
        targets = []

        # loop over the contours
        for c in contours:
            
            # if the contour is too small, ignore it
            if cv2.contourArea(c) < 230:
                    continue

            # contour data
            M = cv2.moments(c)#;print( M )
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            x,y,w,h = cv2.boundingRect(c)
            rx = x+int(w/2)
            ry = y+int(h/2)
            ca = cv2.contourArea(c)

            # plot contours
            cv2.drawContours(frame6,[c],0,(0,0,255),2)
            cv2.rectangle(frame6,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(frame6,(cx,cy),2,(0,0,255),2)
            cv2.circle(frame6,(rx,ry),2,(0,255,0),2)



            # save target contours
            targets.append((cx,cy,ca))
        
        # update master
        master = frame2

        # display
##        cv2.imshow("Frame0: Raw",frame0)
##        cv2.imshow("Frame1: Gray",frame1)
##        cv2.imshow("Frame2: Blur",frame2)
##        cv2.imshow("Frame3: Delta",frame3)
##        cv2.imshow("Frame4: Threshold",frame4)
##        cv2.imshow("Frame5: Dialated",frame5)
        #cv2.imshow("Frame6: Contours",frame6)

        if (n_white_pix1 > 500):
            jum1+=1
        elif (n_white_pix1 < 500):
            jum1=0
        if (jum1 == 5):
            total1+=1

        if (n_white_pix2 > 500):
            jum2+=1
        elif (n_white_pix2 < 500):
            jum2=0
        if (jum2 == 5):
            total2+=1

        if (n_white_pix3 > 500):
            jum3+=1
        elif (n_white_pix3 < 500):
            jum3=0
        if (jum3 == 5):
            total3+=1

        if (n_white_pix4 > 500):
            jum4+=1
        elif (n_white_pix4 < 500):
            jum4=0
        if (jum4 == 5):
            total4+=1
        
        # key delay and action
        key = cv2.waitKey(10) & 0xFF
        
        if key == ord('q'):
            break
        elif key != 255:
            print('key:',[chr(key)])

    # release camera
    camera.release()

        
    # close all windows
    cv2.destroyAllWindows()

    
def seluruh8():
    # init camera
    camera = cv2.VideoCapture('Video/DelapanPDB.mp4')   ### <<<=== SET THE CORRECT CAMERA NUMBER
    camera.set(3,1280)             # set frame width
    camera.set(4,720)              # set frame height
    time.sleep(0.5)
    print(camera.get(3),camera.get(4))

    # master frame
    x_value = 0
    total_1 = 0
    total_2 = 0
    total_3 = 0
    total_4 = 0
    total_5 = 0
    total_6 = 0
    total_7 = 0
    total_8 = 0
    master = None

    fieldnames = ["x_value", "total_1", "total_2", "total_3", "total_4", "total_5", "total_6", "total_7", "total_8"]
    waktu = [0,0,0]
    i=0

    jum1=0
    jum2=0
    jum3=0
    jum4=0
    jum5=0
    jum6=0
    jum7=0
    jum8=0

    total1=0
    total2=0
    total3=0
    total4=0
    total5=0
    total6=0
    total7=0
    total8=0

    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    while 1:

        # grab a frame 10,400),(200,700
        (grabbed,frame) = camera.read()

        frame0 = cv2.resize(frame,(1280, 720)) 
        # end of feed
        if not grabbed:
            break

        # gray frame
        frame1 = cv2.cvtColor(frame0,cv2.COLOR_BGR2GRAY)

        # blur frame
        frame2 = cv2.GaussianBlur(frame1,(15,15),0)

        # initialize master
        if master is None:
            master = frame2
            continue

        # delta frame
        frame3 = cv2.absdiff(master,frame2)

        # threshold frame
        frame4 = cv2.threshold(frame3,15,255,cv2.THRESH_BINARY)[1]

        # dilate the thresholded image to fill in holes
        kernel = np.ones((2,2),np.uint8)
        frame5 = cv2.erode(frame4,kernel,iterations=4)
        frame5 = cv2.dilate(frame5,kernel,iterations=8)
        
        img1 = frame5[50:230,150:350]
        img2 = frame5[50:230,410:610]
        img3 = frame5[50:230,730:930]
        img4 = frame5[50:230,980:1180]
        img5 = frame5[270:450,0:200]
        img6 = frame5[270:450,330:520]
        img7 = frame5[270:450,750:950]
        img8 = frame5[270:450,1080:1280]
        
        n_white_pix1 = np.sum(img1 == 255)
        n_white_pix2 = np.sum(img2 == 255)
        n_white_pix3 = np.sum(img3 == 255)
        n_white_pix4 = np.sum(img4 == 255)
        n_white_pix5 = np.sum(img5 == 255)
        n_white_pix6 = np.sum(img6 == 255)
        n_white_pix7 = np.sum(img7 == 255)
        n_white_pix8 = np.sum(img8 == 255)
        
        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info = {
                "x_value": x_value,
                "total_1": total_1,
                "total_2": total_2,
                "total_3": total_3,
                "total_4": total_4,
                "total_5": total_5,
                "total_6": total_6,
                "total_7": total_7,
                "total_8": total_8
            }
            
            csv_writer.writerow(info)
            print(x_value, total_1, total_2, total_3, total_4, total_5, total_6, total_7, total_8)
                    

            x_value += 1
            total_1 = n_white_pix1
            total_2 = n_white_pix2
            total_3 = n_white_pix3
            total_4 = n_white_pix4
            total_5 = n_white_pix5
            total_6 = n_white_pix6
            total_7 = n_white_pix7
            total_8 = n_white_pix8


        # find contours on thresholded image
        nada,contours,nada = cv2.findContours(frame5.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        # make coutour frame
        frame6 = frame0.copy()
        
        cv2.rectangle(frame6,(150,50),(350,230),(0,255,0),2)
        cv2.rectangle(frame6,(410,50),(610,230),(0,255,0),2)
        cv2.rectangle(frame6,(730,50),(930,230),(0,255,0),2)
        cv2.rectangle(frame6,(980,50),(1180,230),(0,255,0),2)
        cv2.rectangle(frame6,(0,270),(200,450),(0,255,0),2)
        cv2.rectangle(frame6,(330,270),(520,450),(0,255,0),2)
        cv2.rectangle(frame6,(750,270),(950,450),(0,255,0),2)
        cv2.rectangle(frame6,(1080,270),(1280,450),(0,255,0),2)

        cv2.putText(frame6,'Participant 1: '+ str(total1)+' moves', 
            (140,40), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)
        cv2.putText(frame6,'Participant 2: '+str(total2)+' moves', 
            (410,40), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)
        cv2.putText(frame6,'Participant 3: '+str(total3)+' moves', 
            (730,40), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)
        cv2.putText(frame6,'Participant 4: '+str(total4)+' moves', 
            (980,40), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)
        cv2.putText(frame6,'Participant 5: '+ str(total5)+' moves', 
            (0,260), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)
        cv2.putText(frame6,'Participant 6: '+str(total6)+' moves', 
            (330,260), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)
        cv2.putText(frame6,'Participant 7: '+str(total7)+' moves', 
            (750,260), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)
        cv2.putText(frame6,'Participant 8: '+str(total8)+' moves', 
            (1040,260), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)

        if (n_white_pix1>389):
            cv2.rectangle(frame6,(150,50),(350,230),(0,0,255),2)
        if (n_white_pix2>389):
            cv2.rectangle(frame6,(410,50),(610,230),(0,0,255),2)
        if (n_white_pix3>389):
            cv2.rectangle(frame6,(730,50),(930,230),(0,0,255),2)
        if (n_white_pix4>389):
            cv2.rectangle(frame6,(980,50),(1180,230),(0,0,255),2)
        if (n_white_pix5>389):
            cv2.rectangle(frame6,(0,270),(200,450),(0,0,255),2)
        if (n_white_pix6>389):
            cv2.rectangle(frame6,(330,270),(520,450),(0,0,255),2)
        if (n_white_pix7>389):
            cv2.rectangle(frame6,(750,270),(950,450),(0,0,255),2)
        if (n_white_pix8>389):
            cv2.rectangle(frame6,(1080,270),(1280,450),(0,0,255),2)

        # target contours
        targets = []

        # loop over the contours
        for c in contours:
            
            # if the contour is too small, ignore it
            if cv2.contourArea(c) < 230:
                    continue

            # contour data
            M = cv2.moments(c)#;print( M )
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            x,y,w,h = cv2.boundingRect(c)
            rx = x+int(w/2)
            ry = y+int(h/2)
            ca = cv2.contourArea(c)

            # plot contours
            cv2.drawContours(frame6,[c],0,(0,0,255),2)
            cv2.rectangle(frame6,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(frame6,(cx,cy),2,(0,0,255),2)
            cv2.circle(frame6,(rx,ry),2,(0,255,0),2)



            # save target contours
            targets.append((cx,cy,ca))
        
        # update master
        master = frame2
            
        # display
##        cv2.imshow("Frame0: Raw",frame0)
##        cv2.imshow("Frame1: Gray",frame1)
##        cv2.imshow("Frame2: Blur",frame2)
##        cv2.imshow("Frame3: Delta",frame3)
##        cv2.imshow("Frame4: Threshold",frame4)
##        cv2.imshow("Frame5: Dialated",frame5)
        cv2.imshow("Frame6: Contours",frame6)

        if (n_white_pix1 > 500):
            jum1+=1
        elif (n_white_pix1 < 500):
            jum1=0
        if (jum1 == 5):
            total1+=1

        if (n_white_pix2 > 500):
            jum2+=1
        elif (n_white_pix2 < 500):
            jum2=0
        if (jum2 == 5):
            total2+=1

        if (n_white_pix3 > 500):
            jum3+=1
        elif (n_white_pix3 < 500):
            jum3=0
        if (jum3 == 5):
            total3+=1

        if (n_white_pix4 > 500):
            jum4+=1
        elif (n_white_pix4 < 500):
            jum4=0
        if (jum4 == 5):
            total4+=1

        if (n_white_pix5 > 500):
            jum5+=1
        elif (n_white_pix5 < 500):
            jum5=0
        if (jum5 == 5):
            total5+=1

        if (n_white_pix6 > 500):
            jum6+=1
        elif (n_white_pix6 < 500):
            jum6=0
        if (jum6 == 5):
            total6+=1

        if (n_white_pix7 > 500):
            jum7+=1
        elif (n_white_pix7 < 500):
            jum7=0
        if (jum7 == 5):
            total7+=1

        if (n_white_pix8 > 500):
            jum8+=1
        elif (n_white_pix8 < 500):
            jum8=0
        if (jum8 == 5):
            total8+=1
        
        # key delay and action
        key = cv2.waitKey(10) & 0xFF
        
        if key == ord('q'):
            break
        elif key != 255:
            print('key:',[chr(key)])

    # release camera
    camera.release()

        
    # close all windows
    cv2.destroyAllWindows()
     


def bagian1():
    # init camera
    camera = cv2.VideoCapture('Video/roris2.mp4')   ### <<<=== SET THE CORRECT CAMERA NUMBER
    camera.set(3,1280)             # set frame width
    camera.set(4,720)              # set frame height
    time.sleep(0.5)
    print(camera.get(3),camera.get(4))

    # master frame
    x_value = 0
    total_1 = 0
    master = None

    fieldnames = ["x_value", "total_1"]
    jum=0
    total=0

    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        
    while 1:
        
        # grab a frame 10,400),(200,700
        (grabbed,frame) = camera.read()
      
        frame0 = cv2.resize(frame, (1280, 720)) 
        # end of feed
        if not grabbed:
            break

        # gray frame
        frame1 = cv2.cvtColor(frame0,cv2.COLOR_BGR2GRAY)

        # blur frame
        frame2 = cv2.GaussianBlur(frame1,(15,15),0)

        # initialize master
        if master is None:
            master = frame2
            continue

        # delta frame
        frame3 = cv2.absdiff(master,frame2)

        # threshold frame
        frame4 = cv2.threshold(frame3,15,255,cv2.THRESH_BINARY)[1]

        # dilate the thresholded image to fill in holes
        kernel = np.ones((2,2),np.uint8)
        frame5 = cv2.erode(frame4,kernel,iterations=4)
        frame5 = cv2.dilate(frame5,kernel,iterations=8)

        img1 = frame5[300:500,550:750]
        img1kepala = frame5[300:430,550:750]
        img1tangan = frame5[430:500,550:750]
        n_white_pix1 = np.sum(img1 == 255)
        n_white_pix1kepala = np.sum(img1tangan == 255)
        n_white_pix1tangan = np.sum(img1kepala == 255)

        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info = {
                "x_value": x_value,
                "total_1": total_1
            }

            csv_writer.writerow(info)
            print(x_value, total_1, jum, total)
                    
            x_value += 1
            total_1 = n_white_pix1


        # find contours on thresholded image
        nada,contours,nada = cv2.findContours(frame5.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        # make coutour frame
        frame6 = frame0.copy()

        cv2.rectangle(frame6,(550,300),(750,500),(0,255,0),2)
        cv2.rectangle(frame6,(550,300),(750,430),(0,255,0),2)
        cv2.rectangle(frame6,(550,430),(750,500),(0,255,0),2)

        if (n_white_pix1>506):
             cv2.rectangle(frame6,(550,300),(750,500),(0,0,255),2)
             
        #    cv2.rectangle(frame6,(550,300),(750,500),(0,0,255),2)
        if(n_white_pix1kepala>230 and n_white_pix1tangan>230):
            cv2.rectangle(frame6,(550,300),(750,500),(0,0,255),2)
            cv2.putText(frame6,'Seluruh tubuh', 
                (550,290), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix1tangan>230):
            cv2.rectangle(frame6,(550,300),(750,430),(0,0,255),2)
            cv2.putText(frame6,'Kepala', 
                (550,290), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix1kepala>230):
            cv2.rectangle(frame6,(550,430),(750,500),(0,0,255),2)
            cv2.putText(frame6,'Tangan', 
                (550,290), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)

        cv2.putText(frame6,'Participant 1 : ' + str(total) + ' moves', 
                (550,270), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
                    
        # target contours
        targets = []

        # loop over the contours
        for c in contours:
            
            # if the contour is too small, ignore it
            if cv2.contourArea(c) < 230:
                    continue

            # contour data
            M = cv2.moments(c)#;print( M )
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            x,y,w,h = cv2.boundingRect(c)
            rx = x+int(w/2)
            ry = y+int(h/2)
            ca = cv2.contourArea(c)

            # plot contours
            cv2.drawContours(frame6,[c],0,(0,0,255),2)
            cv2.rectangle(frame6,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(frame6,(cx,cy),2,(0,0,255),2)
            cv2.circle(frame6,(rx,ry),2,(0,255,0),2)

            # save target contours
            targets.append((cx,cy,ca))

        
        # update master
        master = frame2

        img2 = frame6[250:550,350:800]

        # display
##        cv2.imshow("Frame0: Raw",frame0)
##        cv2.imshow("Frame1: Gray",frame1)
##        cv2.imshow("Frame2: Blur",frame2)
##        cv2.imshow("Frame3: Delta",frame3)
##        cv2.imshow("Frame4: Threshold",frame4)
##        cv2.imshow("Frame5: Dialated",frame5)
        cv2.imshow("Frame6: Contours",frame6)
      ##  cv2.imshow("Frame7: Crop",img1kepala)
            
        if (n_white_pix1 > 500):
            jum+=1
        elif (n_white_pix1 < 500):
            jum=0
        if (jum == 5):
            total+=1
        

        # key delay and action
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            break
        elif key != 255:
            print('key:',[chr(key)])

    # release camera
    camera.release()

        
    # close all windows
    cv2.destroyAllWindows()
     


def bagian4():
     # init camera
    camera = cv2.VideoCapture('Video/EmpatPSB.mp4')   ### <<<=== SET THE CORRECT CAMERA NUMBER
    camera.set(3,1280)             # set frame width
    camera.set(4,720)              # set frame height
    time.sleep(0.5)
    print(camera.get(3),camera.get(4))

    # master frame
    x_value = 0
    total_1 = 0
    total_2 = 0
    total_3 = 0
    total_4 = 0
    master = None

    fieldnames = ["x_value", "total_1", "total_2", "total_3", "total_4"]
    waktu = [0,0,0]
    i=0

    jum1=0
    jum2=0
    jum3=0
    jum4=0

    total1=0
    total2=0
    total3=0
    total4=0

    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    while 1:
        # grab a frame 10,400),(200,700
        (grabbed,frame) = camera.read()

        frame0 = cv2.resize(frame,(1280, 720)) 
        # end of feed
        if not grabbed:
            break

        # gray frame
        frame1 = cv2.cvtColor(frame0,cv2.COLOR_BGR2GRAY)

        # blur frame
        frame2 = cv2.GaussianBlur(frame1,(15,15),0)

        # initialize master
        if master is None:
            master = frame2
            continue

        # delta frame
        frame3 = cv2.absdiff(master,frame2)

        # threshold frame
        frame4 = cv2.threshold(frame3,15,255,cv2.THRESH_BINARY)[1]

        # dilate the thresholded image to fill in holes
        kernel = np.ones((2,2),np.uint8)
        frame5 = cv2.erode(frame4,kernel,iterations=4)
        frame5 = cv2.dilate(frame5,kernel,iterations=8)
        
        img1 = frame5[280:480,0:230]
        img1kepala = frame5[280:410,0:230]
        img1tangan  = frame5[410:480,0:230]
        
        img2 = frame5[280:480,290:490]
        img2kepala = frame5[280:410,290:490]
        img2tangan = frame5[410:480,290:490]
        
        img3 = frame5[280:480,700:900]
        img3kepala = frame5[280:410,700:900]
        img3tangan = frame5[410:480,700:900]
        
        img4 = frame5[280:480,1080:1280]
        img4kepala = frame5[280:410,1080:1280]
        img4tangan = frame5[410:480,1080:1280]
        
        n_white_pix1 = np.sum(img1 == 255)
        n_white_pix1kepala = np.sum(img1tangan == 255)
        n_white_pix1tangan = np.sum(img1kepala == 255)
        
        n_white_pix2 = np.sum(img2 == 255)
        n_white_pix2kepala = np.sum(img2tangan == 255)
        n_white_pix2tangan = np.sum(img2kepala == 255)
        
        n_white_pix3 = np.sum(img3 == 255)
        n_white_pix3kepala = np.sum(img3tangan == 255)
        n_white_pix3tangan = np.sum(img3kepala == 255)
        
        n_white_pix4 = np.sum(img4 == 255)
        n_white_pix4kepala = np.sum(img4tangan == 255)
        n_white_pix4tangan = np.sum(img4kepala == 255)
        
        
        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info = {
                "x_value": x_value,
                "total_1": total_1,
                "total_2": total_2,
                "total_3": total_3,
                "total_4": total_4
            }
            
            csv_writer.writerow(info)
            print(x_value, total_1, total_2, total_3, total_4)
                    

            x_value += 1
            total_1 = n_white_pix1
            total_2 = n_white_pix2
            total_3 = n_white_pix3
            total_4 = n_white_pix4


        # find contours on thresholded image
        nada,contours,nada = cv2.findContours(frame5.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        # make coutour frame
        frame6 = frame0.copy()
        
        cv2.rectangle(frame6,(0,280),(200,480),(0,255,0),2)
        cv2.rectangle(frame6,(0,280),(200,410),(0,255,0),2)
        cv2.rectangle(frame6,(0,410),(200,480),(0,255,0),2)
        
        cv2.rectangle(frame6,(290,280),(490,480),(0,255,0),2)
        cv2.rectangle(frame6,(290,280),(490,410),(0,255,0),2)
        cv2.rectangle(frame6,(290,410),(490,480),(0,255,0),2)
        
        cv2.rectangle(frame6,(700,280),(900,480),(0,255,0),2)
        cv2.rectangle(frame6,(700,280),(900,410),(0,255,0),2)
        cv2.rectangle(frame6,(700,410),(900,480),(0,255,0),2)
        
        cv2.rectangle(frame6,(1080,280),(1280,480),(0,255,0),2)
        cv2.rectangle(frame6,(1080,280),(1280,410),(0,255,0),2)
        cv2.rectangle(frame6,(1080,410),(1280,480),(0,255,0),2)

        if(n_white_pix1kepala>230 and n_white_pix1tangan>230):
            cv2.rectangle(frame6,(0,280),(200,480),(0,0,255),2)
            cv2.putText(frame6,'Seluruh tubuh', 
                (0,270), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix1tangan>230):
            cv2.rectangle(frame6,(0,280),(200,410),(0,0,255),2)
            cv2.putText(frame6,'Kepala', 
                (0,270), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix1kepala>230):
            cv2.rectangle(frame6,(0,410),(200,480),(0,0,255),2)
            cv2.putText(frame6,'Tangan', 
                (0,270), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)

        cv2.putText(frame6,'Participant 1: '+ str(total1)+' moves', 
            (0,250), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)


        if(n_white_pix2kepala>230 and n_white_pix2tangan>230):
            cv2.rectangle(frame6,(290,280),(490,480),(0,0,255),2)
            cv2.putText(frame6,'Seluruh tubuh', 
                (290,270), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix2tangan>230):
            cv2.rectangle(frame6,(290,280),(490,410),(0,0,255),2)
            cv2.putText(frame6,'Kepala', 
                (290,270), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix2kepala>230):
            cv2.rectangle(frame6,(290,410),(490,480),(0,0,255),2)
            cv2.putText(frame6,'Tangan', 
                (290,270), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        
        cv2.putText(frame6,'Participant 2: '+str(total2)+' moves', 
            (290,250), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)

        if(n_white_pix3kepala>230 and n_white_pix3tangan>230):
            cv2.rectangle(frame6,(700,280),(900,480),(0,0,255),2)
            cv2.putText(frame6,'Seluruh tubuh', 
                (700,270), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix3tangan>230):
            cv2.rectangle(frame6,(700,280),(900,410),(0,0,255),2)
            cv2.putText(frame6,'Kepala', 
                (700,270), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix3kepala>230):
            cv2.rectangle(frame6,(700,410),(900,480),(0,0,255),2)
            cv2.putText(frame6,'Tangan', 
                (700,270), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
            
        cv2.putText(frame6,'Participant 3: '+str(total3)+' moves', 
            (700,250), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)

        if(n_white_pix4kepala>230 and n_white_pix4tangan>230):
            cv2.rectangle(frame6,(1080,280),(1280,480),(0,0,255),2)
            cv2.putText(frame6,'Seluruh tubuh', 
                (1080,270), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix4tangan>230):
            cv2.rectangle(frame6,(1080,280),(1280,410),(0,0,255),2)
            cv2.putText(frame6,'Kepala', 
                (1080,270), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix4kepala>230):
            cv2.rectangle(frame6,(1080,410),(1280,480),(0,0,255),2)
            cv2.putText(frame6,'Tangan', 
                (1080,270), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
            
        cv2.putText(frame6,'Participant 4: '+str(total4)+' moves', 
            (1030,250), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)

        # target contours
        targets = []

        # loop over the contours
        for c in contours:
            
            # if the contour is too small, ignore it
            if cv2.contourArea(c) < 230:
                    continue

            # contour data
            M = cv2.moments(c)#;print( M )
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            x,y,w,h = cv2.boundingRect(c)
            rx = x+int(w/2)
            ry = y+int(h/2)
            ca = cv2.contourArea(c)

            # plot contours
            cv2.drawContours(frame6,[c],0,(0,0,255),2)
            cv2.rectangle(frame6,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(frame6,(cx,cy),2,(0,0,255),2)
            cv2.circle(frame6,(rx,ry),2,(0,255,0),2)



            # save target contours
            targets.append((cx,cy,ca))

        
        # update master
        master = frame2

##        # display
##        cv2.imshow("Frame0: Raw",frame0)
##        cv2.imshow("Frame1: Gray",frame1)
##        cv2.imshow("Frame2: Blur",frame2)
##        cv2.imshow("Frame3: Delta",frame3)
##        cv2.imshow("Frame4: Threshold",frame4)
##        cv2.imshow("Frame5: Dialated",frame5)
        cv2.imshow("Frame6: Contours",frame6)

        if (n_white_pix1 > 500):
            jum1+=1
        elif (n_white_pix1 < 500):
            jum1=0
        if (jum1 == 5):
            total1+=1

        if (n_white_pix2 > 500):
            jum2+=1
        elif (n_white_pix2 < 500):
            jum2=0
        if (jum2 == 5):
            total2+=1

        if (n_white_pix3 > 500):
            jum3+=1
        elif (n_white_pix3 < 500):
            jum3=0
        if (jum3 == 5):
            total3+=1

        if (n_white_pix4 > 500):
            jum4+=1
        elif (n_white_pix4 < 500):
            jum4=0
        if (jum4 == 5):
            total4+=1
       
        # key delay and action
        key = cv2.waitKey(10) & 0xFF
        
        if key == ord('q'):
            break
        elif key != 255:
            print('key:',[chr(key)])

    # release camera
    camera.release()

        
    # close all windows
    cv2.destroyAllWindows()
     


def bagian8():
    # init camera
    camera = cv2.VideoCapture('Video/DelapanPDB.mp4')   ### <<<=== SET THE CORRECT CAMERA NUMBER
    camera.set(3,1280)             # set frame width
    camera.set(4,720)              # set frame height
    time.sleep(0.5)
    print(camera.get(3),camera.get(4))

    # master frame
    x_value = 0
    total_1 = 0
    total_2 = 0
    total_3 = 0
    total_4 = 0
    total_5 = 0
    total_6 = 0
    total_7 = 0
    total_8 = 0
    master = None

    fieldnames = ["x_value", "total_1", "total_2", "total_3", "total_4", "total_5", "total_6", "total_7", "total_8"]
    waktu = [0,0,0]
    i=0

    jum1=0
    jum2=0
    jum3=0
    jum4=0
    jum5=0
    jum6=0
    jum7=0
    jum8=0

    total1=0
    total2=0
    total3=0
    total4=0
    total5=0
    total6=0
    total7=0
    total8=0

    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    while 1:      
        # grab a frame 10,400),(200,700
        (grabbed,frame) = camera.read()

        frame0 = cv2.resize(frame,(1280, 720)) 
        # end of feed
        if not grabbed:
            break

        # gray frame
        frame1 = cv2.cvtColor(frame0,cv2.COLOR_BGR2GRAY)

        # blur frame
        frame2 = cv2.GaussianBlur(frame1,(15,15),0)

        # initialize master
        if master is None:
            master = frame2
            continue

        # delta frame
        frame3 = cv2.absdiff(master,frame2)

        # threshold frame
        frame4 = cv2.threshold(frame3,15,255,cv2.THRESH_BINARY)[1]

        # dilate the thresholded image to fill in holes
        kernel = np.ones((2,2),np.uint8)
        frame5 = cv2.erode(frame4,kernel,iterations=4)
        frame5 = cv2.dilate(frame5,kernel,iterations=8)
        
        img1 = frame5[50:230,150:350]
        img1kepala = frame5[50:160,150:350]
        img1tangan = frame5[160:230,150:350]
        
        img2 = frame5[50:230,410:610]
        img2kepala = frame5[50:160,410:610]
        img2tangan = frame5[160:230,410:610]
        
        img3 = frame5[50:230,730:930]
        img3kepala = frame5[50:160,730:930]
        img3tangan = frame5[160:230,730:930]
        
        img4 = frame5[50:230,980:1180]
        img4kepala = frame5[50:160,980:1180]
        img4tangan = frame5[160:230,980:1180]
        
        img5 = frame5[270:450,0:200]
        img5kepala = frame5[270:380,0:200]
        img5tangan = frame5[380:450,0:200]
        
        img6 = frame5[270:450,330:520]
        img6kepala = frame5[270:380,330:520]
        img6tangan = frame5[380:450,330:520]
        
        img7 = frame5[270:450,750:950]
        img7kepala = frame5[270:380,750:950]
        img7tangan = frame5[380:450,750:950]

        img8 = frame5[270:450,1080:1280]
        img8kepala = frame5[270:380,1080:1280]
        img8tangan = frame5[380:450,1080:1280]
        
        n_white_pix1 = np.sum(img1 == 255)
        n_white_pix1kepala = np.sum(img1tangan == 255)
        n_white_pix1tangan = np.sum(img1kepala == 255)
        
        n_white_pix2 = np.sum(img2 == 255)
        n_white_pix2kepala = np.sum(img2tangan == 255)
        n_white_pix2tangan = np.sum(img2kepala == 255)
        
        n_white_pix3 = np.sum(img3 == 255)
        n_white_pix3kepala = np.sum(img3tangan == 255)
        n_white_pix3tangan = np.sum(img3kepala == 255)
        
        n_white_pix4 = np.sum(img4 == 255)
        n_white_pix4kepala = np.sum(img4tangan == 255)
        n_white_pix4tangan = np.sum(img4kepala == 255)
        
        n_white_pix5 = np.sum(img5 == 255)
        n_white_pix5kepala = np.sum(img5tangan == 255)
        n_white_pix5tangan = np.sum(img5kepala == 255)
        
        n_white_pix6 = np.sum(img6 == 255)
        n_white_pix6kepala = np.sum(img6tangan == 255)
        n_white_pix6tangan = np.sum(img6kepala == 255)
        
        n_white_pix7 = np.sum(img7 == 255)
        n_white_pix7kepala = np.sum(img7tangan == 255)
        n_white_pix7tangan = np.sum(img7kepala == 255)
        
        n_white_pix8 = np.sum(img8 == 255)
        n_white_pix8kepala = np.sum(img8tangan == 255)
        n_white_pix8tangan = np.sum(img8kepala == 255)
        
        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info = {
                "x_value": x_value,
                "total_1": total_1,
                "total_2": total_2,
                "total_3": total_3,
                "total_4": total_4,
                "total_5": total_5,
                "total_6": total_6,
                "total_7": total_7,
                "total_8": total_8
            }
            
            csv_writer.writerow(info)
            print(x_value, total_1, total_2, total_3, total_4, total_5, total_6, total_7, total_8)
                    

            x_value += 1
            total_1 = n_white_pix1
            total_2 = n_white_pix2
            total_3 = n_white_pix3
            total_4 = n_white_pix4
            total_5 = n_white_pix5
            total_6 = n_white_pix6
            total_7 = n_white_pix7
            total_8 = n_white_pix8


        # find contours on thresholded image
        nada,contours,nada = cv2.findContours(frame5.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        # make coutour frame
        frame6 = frame0.copy()
        
        cv2.rectangle(frame6,(150,50),(350,230),(0,255,0),2)
        cv2.rectangle(frame6,(150,50),(350,160),(0,255,0),2)
        cv2.rectangle(frame6,(150,160),(350,230),(0,255,0),2)
        
        cv2.rectangle(frame6,(410,50),(610,230),(0,255,0),2)
        cv2.rectangle(frame6,(410,50),(610,160),(0,255,0),2)
        cv2.rectangle(frame6,(410,160),(610,230),(0,255,0),2)
        
        cv2.rectangle(frame6,(730,50),(930,230),(0,255,0),2)
        cv2.rectangle(frame6,(730,50),(930,160),(0,255,0),2)
        cv2.rectangle(frame6,(730,160),(930,230),(0,255,0),2)
        
        cv2.rectangle(frame6,(980,50),(1180,230),(0,255,0),2)
        cv2.rectangle(frame6,(980,50),(1180,160),(0,255,0),2)
        cv2.rectangle(frame6,(980,160),(1180,230),(0,255,0),2)
        
        cv2.rectangle(frame6,(0,270),(200,450),(0,255,0),2)
        cv2.rectangle(frame6,(0,270),(200,380),(0,255,0),2)
        cv2.rectangle(frame6,(0,380),(200,450),(0,255,0),2)
        
        cv2.rectangle(frame6,(330,270),(520,450),(0,255,0),2)
        cv2.rectangle(frame6,(330,270),(520,380),(0,255,0),2)
        cv2.rectangle(frame6,(330,380),(520,450),(0,255,0),2)
        
        cv2.rectangle(frame6,(750,270),(950,450),(0,255,0),2)
        cv2.rectangle(frame6,(750,270),(950,380),(0,255,0),2)
        cv2.rectangle(frame6,(750,380),(950,450),(0,255,0),2)
        
        cv2.rectangle(frame6,(1080,270),(1280,450),(0,255,0),2)
        cv2.rectangle(frame6,(1080,270),(1280,380),(0,255,0),2)
        cv2.rectangle(frame6,(1080,380),(1280,450),(0,255,0),2)

        if(n_white_pix1kepala>230 and n_white_pix1tangan>230):
            cv2.rectangle(frame6,(150,50),(350,230),(0,0,255),2)
            cv2.putText(frame6,'Seluruh tubuh', 
                (140,40), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix1tangan>230):
            cv2.rectangle(frame6,(150,50),(350,160),(0,0,255),2)
            cv2.putText(frame6,'Kepala', 
                (140,40), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix1kepala>230):
            cv2.rectangle(frame6,(150,160),(350,230),(0,0,255),2)
            cv2.putText(frame6,'Tangan', 
                (140,40), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
            
        cv2.putText(frame6,'Participant 1: '+ str(total1)+' moves', 
            (140,20), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)
        
        if(n_white_pix2kepala>230 and n_white_pix2tangan>230):
            cv2.rectangle(frame6,(410,50),(610,230),(0,0,255),2)
            cv2.putText(frame6,'Seluruh tubuh', 
                (410,40), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix2tangan>230):
            cv2.rectangle(frame6,(410,50),(610,160),(0,0,255),2)
            cv2.putText(frame6,'Kepala', 
                (410,40), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix2kepala>230):
            cv2.rectangle(frame6,(410,160),(610,230),(0,0,255),2)
            cv2.putText(frame6,'Tangan', 
                (410,40), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
            
        cv2.putText(frame6,'Participant 2: '+str(total2)+' moves', 
            (410,20), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)

        if(n_white_pix3kepala>230 and n_white_pix3tangan>230):
            cv2.rectangle(frame6,(730,50),(930,230),(0,0,255),2)
            cv2.putText(frame6,'Seluruh tubuh', 
                (730,40), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix3tangan>230):
            cv2.rectangle(frame6,(730,50),(930,160),(0,0,255),2)
            cv2.putText(frame6,'Kepala', 
                (730,40), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix3kepala>230):
            cv2.rectangle(frame6,(730,160),(930,230),(0,0,255),2)
            cv2.putText(frame6,'Tangan', 
                (730,40), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
            
        cv2.putText(frame6,'Participant 3: '+str(total3)+' moves', 
            (730,20), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)

        if(n_white_pix4kepala>230 and n_white_pix4tangan>230):
            cv2.rectangle(frame6,(980,50),(1180,230),(0,0,255),2)
            cv2.putText(frame6,'Seluruh tubuh', 
                (980,40), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix4tangan>230):
            cv2.rectangle(frame6,(980,50),(1180,160),(0,0,255),2)
            cv2.putText(frame6,'Kepala', 
                (980,40), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix4kepala>230):
            cv2.rectangle(frame6,(980,160),(1180,230),(0,0,255),2)
            cv2.putText(frame6,'Tangan', 
                (980,40), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
            
        cv2.putText(frame6,'Participant 4: '+str(total4)+' moves', 
            (980,20), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)
        
        if(n_white_pix5kepala>230 and n_white_pix5tangan>230):
            cv2.rectangle(frame6,(0,270),(200,450),(0,0,255),2)
            cv2.putText(frame6,'Seluruh tubuh', 
                (0,470), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix5tangan>230):
            cv2.rectangle(frame6,(0,270),(200,380),(0,0,255),2)
            cv2.putText(frame6,'Kepala', 
                (0,470), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix5kepala>230):
            cv2.rectangle(frame6,(0,380),(200,450),(0,0,255),2)
            cv2.putText(frame6,'Tangan', 
                (0,470), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
            
        cv2.putText(frame6,'Participant 5: '+ str(total5)+' moves', 
            (0,490), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)
        
        if(n_white_pix6kepala>230 and n_white_pix6tangan>230):
            cv2.rectangle(frame6,(330,270),(520,450),(0,0,255),2)
            cv2.putText(frame6,'Seluruh tubuh', 
                (330,470), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix6tangan>230):
            cv2.rectangle(frame6,(330,270),(520,380),(0,0,255),2)
            cv2.putText(frame6,'Kepala', 
                (330,470), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix6kepala>230):
            cv2.rectangle(frame6,(330,380),(520,450),(0,0,255),2)
            cv2.putText(frame6,'Tangan', 
                (330,470), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
            
        cv2.putText(frame6,'Participant 6: '+str(total6)+' moves', 
            (330,490), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)

        if(n_white_pix7kepala>230 and n_white_pix7tangan>230):
            cv2.rectangle(frame6,(750,270),(950,450),(0,0,255),2)
            cv2.putText(frame6,'Seluruh tubuh', 
                (750,470), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix7tangan>230):
            cv2.rectangle(frame6,(750,270),(950,380),(0,0,255),2)
            cv2.putText(frame6,'Kepala', 
                (750,470), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix7kepala>230):
            cv2.rectangle(frame6,(750,380),(950,450),(0,0,255),2)
            cv2.putText(frame6,'Tangan', 
                (750,470), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
            
        cv2.putText(frame6,'Participant 7: '+str(total7)+' moves', 
            (750,490), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)

        if(n_white_pix8kepala>230 and n_white_pix8tangan>230):
            cv2.rectangle(frame6,(1080,270),(1280,450),(0,0,255),2)
            cv2.putText(frame6,'Seluruh tubuh', 
                (1040,470), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix8tangan>230):
            cv2.rectangle(frame6,(1080,270),(1280,380),(0,0,255),2)
            cv2.putText(frame6,'Kepala', 
                (1040,470), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        elif (n_white_pix8kepala>230):
            cv2.rectangle(frame6,(1080,380),(1280,450),(0,0,255),2)
            cv2.putText(frame6,'Tangan', 
                (1040,470), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.65,
                (255,255,255),
                2)
        cv2.putText(frame6,'Participant 8: '+str(total8)+' moves', 
            (1040,490), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.65,
            (255,255,255),
            2)

        # target contours
        targets = []

        # loop over the contours
        for c in contours:
            
            # if the contour is too small, ignore it
            if cv2.contourArea(c) < 230:
                    continue

            # contour data
            M = cv2.moments(c)#;print( M )
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            x,y,w,h = cv2.boundingRect(c)
            rx = x+int(w/2)
            ry = y+int(h/2)
            ca = cv2.contourArea(c)

            # plot contours
            cv2.drawContours(frame6,[c],0,(0,0,255),2)
            cv2.rectangle(frame6,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(frame6,(cx,cy),2,(0,0,255),2)
            cv2.circle(frame6,(rx,ry),2,(0,255,0),2)



            # save target contours
            targets.append((cx,cy,ca))
        
        # update master
        master = frame2
            
        # display
##        cv2.imshow("Frame0: Raw",frame0)
##        cv2.imshow("Frame1: Gray",frame1)
##        cv2.imshow("Frame2: Blur",frame2)
##        cv2.imshow("Frame3: Delta",frame3)
##        cv2.imshow("Frame4: Threshold",frame4)
##        cv2.imshow("Frame5: Dialated",frame5)
        #cv2.imshow("Frame6: Contours",frame6)

        if (n_white_pix1 > 500):
            jum1+=1
        elif (n_white_pix1 < 500):
            jum1=0
        if (jum1 == 5):
            total1+=1

        if (n_white_pix2 > 500):
            jum2+=1
        elif (n_white_pix2 < 500):
            jum2=0
        if (jum2 == 5):
            total2+=1

        if (n_white_pix3 > 500):
            jum3+=1
        elif (n_white_pix3 < 500):
            jum3=0
        if (jum3 == 5):
            total3+=1

        if (n_white_pix4 > 500):
            jum4+=1
        elif (n_white_pix4 < 500):
            jum4=0
        if (jum4 == 5):
            total4+=1

        if (n_white_pix5 > 500):
            jum5+=1
        elif (n_white_pix5 < 500):
            jum5=0
        if (jum5 == 5):
            total5+=1

        if (n_white_pix6 > 500):
            jum6+=1
        elif (n_white_pix6 < 500):
            jum6=0
        if (jum6 == 5):
            total6+=1

        if (n_white_pix7 > 500):
            jum7+=1
        elif (n_white_pix7 < 500):
            jum7=0
        if (jum7 == 5):
            total7+=1

        if (n_white_pix8 > 500):
            jum8+=1
        elif (n_white_pix8 < 500):
            jum8=0
        if (jum8 == 5):
            total8+=1

        # key delay and action
        key = cv2.waitKey(10) & 0xFF
        
        if key == ord('q'):
            break
        elif key != 255:
            print('key:',[chr(key)])

    # release camera
    camera.release()

        
    # close all windows
    cv2.destroyAllWindows()
 


def tryto1():
    import random
    from itertools import count
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    plt.style.use('fivethirtyeight')

    index = count()


    def animate(i):
        data = pd.read_csv('data.csv')
        x = data['x_value']
        y1 = data['total_1']
        numb = x.tolist()


        plt.cla()

        plt.plot(x, y1, linewidth=1)
        plt.plot([1, numb[-1]], [500,500],'r-.', linewidth=2)

        plt.xlabel('Frame')
        plt.ylabel('Number of pixels change')
        plt.title('Testing for One Participant')
        plt.grid(True)
        #print(numb[-1])
        
        plt.tight_layout()


    ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    plt.tight_layout()
    plt.show()


def tryto4():
    import random
    from itertools import count
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    plt.style.use('fivethirtyeight')

    x_vals = []
    y_vals = []

    index = count()

    def animate(i):
        data = pd.read_csv('data.csv')
        x = data['x_value']
        y1 = data['total_1']
        y2 = data['total_2']
        y3 = data['total_3']
        y4 = data['total_4']
        numb = x.tolist()

        plt.clf()

        plt.subplot(4, 1, 1)
        plt.plot(x, y1,'r', linewidth=1,)
        plt.plot([0, numb[-1]], [500,500],'k-.', linewidth=2)
        plt.grid(True)
        plt.legend(['Participant 1'])
        plt.subplot(4, 1, 2)
        plt.plot(x, y2,'b', linewidth=1)
        plt.plot([0, numb[-1]], [500,500],'k-.', linewidth=2)
        plt.ylabel('Number of Pixel Changes')
        plt.grid(True)
        plt.legend(['Participant 2'])
        plt.subplot(4, 1, 3)
        plt.plot(x, y3,'g', linewidth=1)
        plt.plot([0, numb[-1]], [500,500],'k-.', linewidth=2)
        plt.grid(True)
        plt.legend(['Participant 3'])
        plt.subplot(4, 1, 4)
        plt.plot(x, y4,'y', linewidth=1)
        plt.plot([0, numb[-1]], [500,500],'k-.', linewidth=2)
        plt.xlabel('Frame number')
        plt.grid(True)
        plt.legend(['Participant 4'])

    ani = FuncAnimation(plt.gcf(), animate, interval=1000)


    plt.tight_layout()
    plt.show()

def tryto8():
    import random
    from itertools import count
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    plt.style.use('fivethirtyeight')

    x_vals = []
    y_vals = []

    index = count()

    def animate(i):
        data = pd.read_csv('data.csv')
        x = data['x_value']
        y1 = data['total_1']
        y2 = data['total_2']
        y3 = data['total_3']
        y4 = data['total_4']
        y5 = data['total_5']
        y6 = data['total_6']
        y7 = data['total_7']
        y8 = data['total_8']
        numb = x.tolist()

        plt.clf()

        plt.subplot(4, 2, 1)
        
        plt.plot(x, y1,'r', linewidth=1,)
        plt.plot([0, numb[-1]], [500,500],'k-.', linewidth=2)
        plt.grid(True)
        plt.legend(['Participant 1'])
        plt.subplot(4, 2, 3)
        plt.plot(x, y2,'b', linewidth=1)
        plt.plot([0, numb[-1]], [500,500],'k-.', linewidth=2)
        plt.ylabel('Number of Pixel Changes')
        plt.grid(True)
        plt.legend(['Participant 2'])
        plt.subplot(4, 2, 5)
        plt.plot(x, y3,'g', linewidth=1)
        plt.plot([0, numb[-1]], [500,500],'k-.', linewidth=2)
        plt.grid(True)
        plt.legend(['Participant 3'])
        plt.subplot(4, 2, 7)
        plt.plot(x, y4,'tab:pink', linewidth=1)
        plt.plot([0, numb[-1]], [500,500],'k-.', linewidth=2)
        plt.xlabel('Frame number')
        plt.grid(True)
        plt.legend(['Participant 4'])
        plt.subplot(4, 2, 2)
        plt.plot(x, y5,'m', linewidth=1,)
        plt.plot([0, numb[-1]], [500,500],'k-.', linewidth=2)
        plt.grid(True)
        plt.legend(['Participant 5'])
        plt.subplot(4, 2, 4)
        plt.plot(x, y6,'y', linewidth=1)
        plt.plot([0, numb[-1]], [500,500],'k-.', linewidth=2)
        plt.ylabel('Number of Pixel Changes')
        plt.grid(True)
        plt.legend(['Participant 6'])
        plt.subplot(4, 2, 6)
        plt.plot(x, y7,'c', linewidth=1)
        plt.plot([0, numb[-1]], [500,500],'k-.', linewidth=2)
        plt.grid(True)
        plt.legend(['Participant 7'])
        plt.subplot(4, 2, 8)
        plt.plot(x, y8,'tab:gray', linewidth=1)
        plt.plot([0, numb[-1]], [500,500],'k-.', linewidth=2)
        plt.xlabel('Frame number')
        plt.grid(True)
        plt.legend(['Participant 8'])

    ani = FuncAnimation(plt.gcf(), animate, interval=1000)


    plt.tight_layout()
    plt.show()



def seluruh1plot():
    Thread(target= seluruh1).start() 
    Thread(target= tryto1).start() 

def seluruh4plot():
    Thread(target= seluruh4).start() 
    Thread(target= tryto4).start()

def seluruh8plot():
    Thread(target= seluruh8).start() 
    Thread(target= tryto8).start() 

def bagian1plot():
    Thread(target= bagian1).start() 
    Thread(target= tryto1).start()

def bagian4plot():
    Thread(target= bagian4).start() 
    Thread(target= tryto4).start() 

def bagian8plot():
    Thread(target= bagian8).start() 
    Thread(target= tryto8).start()

    

