#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 10:03:28 2017

@author: hsagarthegr8
"""

import databasehelper as db
cnx = db.connect()
db.set_database(cnx,'RJIT')
def auth_table():
    auth_table = (
        "CREATE TABLE `auth` ("
        "`username` varchar(12) NOT NULL ,"
        "`password` varchar(12) NOT NULL ,"
        " PRIMARY KEY (`username`)"
        ") ENGINE=InnoDB")
    cursor = cnx.cursor()
    try:
        print("Creating table `auth`: ", end='')
        cursor.execute(auth_table)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
    try:
        cursor.execute("INSERT into `auth` VALUES('root','12345')")
        cnx.commit()
    except mysql.connector.Error as err:
        print(err.msg)
    cursor.close()