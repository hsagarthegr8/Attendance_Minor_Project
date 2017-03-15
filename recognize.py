#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 23:08:33 2017

@author: hsagarthegr8
"""

import databasehelper as db
import cv2
cnx = db.connect()
db.set_database(cnx)
faceDetect = cv2.CascadeClassifier('Cascade/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('Recognizer/trainingData.yaml')

id = 0
#font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)
marked = False

while True:
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf = recognizer.predict(gray[y:y+h,x:x+w])
        #cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255)
        db.mark_attendance(cnx,str(id))
        marked = True
    cv2.imshow('My Face',img)
    if cv2.waitKey(1)==ord('q') or marked:
        break

cam.release()
cv2.destroyAllWindows()
