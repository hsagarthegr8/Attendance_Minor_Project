#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 20:03:32 2017

@author: hsagarthegr8
"""
import os

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
import numpy as np
from PIL import Image

def get_faces_with_username(root_path):
    usernames = os.listdir(root_path)
    faces = []
    users = []
    for username in usernames:
        path_to_faces = os.path.join(root_path,username)
        faces_path = [os.path.join(path_to_faces,img) for img in os.listdir(path_to_faces)]
        for face in faces_path:
            face_img = Image.open(face)
            face_np = np.array(face_img, 'uint8')
            faces.append(face_np)
            users.append(username)
    return np.array(users), faces
