# -*- coding: utf-8 -*-

import cv2,helper,os
import databasehelper as db

def facedetect():
    face_cascade = cv2.CascadeClassifier('Cascade/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('Cascade/haarcascade_eye.xml')
    cam = cv2.VideoCapture(1)
    
    while True:
        ret,img = cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        for x,y,w,h in faces:
            gray_face = cv2.resize((gray[y: y+h, x:x+w]),(110,110))
            eyes = eye_cascade.detectMultiScale(gray_face)
            for ex,ey,ew,eh in eyes:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('My Face',img)
        if cv2.waitKey(1)==ord('q'):
            break
    
    cam.release()
    cv2.destroyAllWindows()
    
def create_dataset(teacher_id):
    faceDetect = cv2.CascadeClassifier('Cascade/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('Cascade/haarcascade_eye.xml')
    cam = cv2.VideoCapture(1)
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
            gray_face = cv2.resize((gray[y: y+h, x:x+w]),(110,110))
            eyes = eye_cascade.detectMultiScale(gray_face)
            for ex,ey,ew,eh in eyes:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
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
    recognizer = cv2.createLBPHFaceRecognizer(2,2,7,7,15)
    path = 'Training'
    userIDs, faces = helper.get_faces_with_username(path)
    recognizer.train(faces,userIDs)
    directory = 'Recognizer'
    helper.ensure_dir(directory)
    recognizer.save('Recognizer/trainingData.yaml')
    
    
def recognize(mark = False):
    faceDetect = cv2.CascadeClassifier('Cascade/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('Cascade/haarcascade_eye.xml')
    cam = cv2.VideoCapture(1)
    recognizer = cv2.createLBPHFaceRecognizer(2,2,7,7,15)
    recognizer.load('Recognizer/trainingData.yaml')
    id = 0
    font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)
    marked = False
    name = None
    while True:
        ret,img = cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        faces = faceDetect.detectMultiScale(gray,1.3,5)
        for x,y,w,h in faces:
            gray_face = cv2.resize((gray[y: y+h, x:x+w]),(110,110))
            eyes = eye_cascade.detectMultiScale(gray_face)
            for ex,ey,ew,eh in eyes:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,conf = recognizer.predict(gray[y:y+h,x:x+w])
                cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255)
                print conf
                if mark and id != -1:
                    name = db.markUtil(id)
                    marked = True
        cv2.imshow('My Face',img)
        if cv2.waitKey(1)==ord('q') or marked:
            break
    cam.release()
    cv2.destroyAllWindows()
    return name,id
