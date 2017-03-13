#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:48:33 2017

@author: hsagarthegr8
"""

import cv2
import helper

recognizer = cv2.face.createLBPHFaceRecognizer()
path = 'Training'

userIDs, faces = helper.get_faces_with_username(path)
recognizer.train(faces,userIDs)
directory = 'Recognizer'
helper.ensure_dir(directory)
recognizer.save(directory + '/' + ' trainingData.yml')