# -*- coding: utf-8 -*-

import cv2,helper,os
import databasehelper as db

def facedetect():
    faceDetect = cv2.CascadeClassifier('Cascade/haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    
    while True:
        ret,img = cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        faces = faceDetect.detectMultiScale(gray,1.3,5)
        for x,y,w,h in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('My Face',img)
        if cv2.waitKey(1)==ord('q'):
            break
    
    cam.release()
    cv2.destroyAllWindows()
    
def create_dataset(teacher_id):
    faceDetect = cv2.CascadeClassifier('Cascade/haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    sample_count = 0
    helper.ensure_dir('Training/')
    directory = 'Training/' + teacher_id + '/'
    helper.ensure_dir(directory)
    s = len(os.listdir(directory))
    while True:
        ret,img = cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        faces = faceDetect.detectMultiScale(gray,1.3,5)
        
        for x,y,w,h in faces:
            sample_count += 1
            cv2.imwrite(directory + teacher_id + '_' + str(sample_count+s) + '.jpg', gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.waitKey(100)
            
        cv2.imshow('My Face',img)
        cv2.waitKey(1)
        if sample_count >= 20:
            break
    cam.release()
    cv2.destroyAllWindows()
    
def train():
    recognizer = cv2.createLBPHFaceRecognizer()
    path = 'Training'
    userIDs, faces = helper.get_faces_with_username(path)
    recognizer.train(faces,userIDs)
    directory = 'Recognizer'
    helper.ensure_dir(directory)
    recognizer.save('Recognizer/trainingData.yaml')
    
    
def recognize(mark = False):
    faceDetect = cv2.CascadeClassifier('Cascade/haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    recognizer = cv2.createLBPHFaceRecognizer()
    recognizer.load('Recognizer/trainingData.yaml')
    id = 0
    font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)
    marked = False
    
    while True:
        ret,img = cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        faces = faceDetect.detectMultiScale(gray,1.3,5)
        for x,y,w,h in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id,conf = recognizer.predict(gray[y:y+h,x:x+w])
            cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255)
            if mark:
                cnx = db.connect()
                cnx.database = 'RJIT'
                db.mark_attendance(cnx,str(id))
                cnx.close()
                marked = True
        cv2.imshow('My Face',img)
        if cv2.waitKey(1)==ord('q') or marked:
            break
    
    cam.release()
    cv2.destroyAllWindows()
