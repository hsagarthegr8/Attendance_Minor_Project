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
        
