#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 23:30:52 2017

@author: hsagarthegr8
"""

import mysql.connector
from mysql.connector import errorcode

def connect():
    '''This function connects the application to the mysql database.'''
    config = {
      'user': 'root',
      'password': 'mytechworld',
      'host': '127.0.0.1',
      'unix_socket': '/opt/lampp/var/mysql/mysql.sock',
      'raise_on_warnings': True,
    }
    cnx = mysql.connector.connect(**config)
    return cnx
    
def create_database(cursor,db):
    '''This function create a database.'''
    print("Creating Database '{}'...".format(db))
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db))
        print("Database '{}' created successfully...".format(db))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        
def set_database(cnx,db):
    '''This function sets the working database to the cnx object.'''
    try:
        cnx.database = db
        print("Current Database is set to '{}'".format(db))
    except mysql.connector.Error as err:
        print("Database '{}' not exists...".format(db))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            cursor = cnx.cursor()
            create_database(cursor,db)
            cnx.database = db
            print("Current Database is set to '{}'".format(db))
        else:
            print(err)
            exit(1)




