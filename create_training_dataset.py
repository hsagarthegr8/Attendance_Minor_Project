#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 22:10:21 2017

@author: hsagarthegr8
"""
import databasehelper as db
import cv2, helper
faceDetect = cv2.CascadeClassifier('Cascade/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

teacher_id = raw_input('Enter teacher_id: ')
first_name = raw_input('Enter first_name: ')
last_name = raw_input('Enter last_name: ')
gender = raw_input('Enter gender (M/F): ')
joining_date = raw_input('Enter joining_date (yyyy-mm-dd): ')
department = raw_input('Enter department: ')
designation = raw_input('Enter designation: ')

sample_count = 0

while True:
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    
    directory = 'Training/' + teacher_id + '/'
    helper.ensure_dir(directory)
    
    for x,y,w,h in faces:
        sample_count += 1
        cv2.imwrite(directory + teacher_id + '_' + str(sample_count) + '.jpg', gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
        
    cv2.imshow('My Face',img)
    cv2.waitKey(1)
    if sample_count >= 20:
        break
cam.release()
cv2.destroyAllWindows()
cnx = db.connect()
db.set_database(cnx)
db.add_teacher(cnx,teacher_id,first_name,last_name,gender,joining_date,department,designation)
cnx.close()

