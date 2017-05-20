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
    print "Creating Database '{}'...".format(db)
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db))
        print "Database '{}' created successfully...".format(db)
    except mysql.connector.Error as err:
        print "Failed creating database: {}".format(err)


def set_database(db='RJIT'):
    '''This function sets the working database to the cnx object.'''
    cnx = connect()
    try:
        cnx.database = db
        print "Current Database is set to '{}'".format(db)
    except mysql.connector.Error as err:
        print "Database '{}' not exists...".format(db)
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            cursor = cnx.cursor()
            create_database(cursor,db)
            cnx.database = db
            print "Current Database is set to '{}'".format(db)
            cursor.close()
            create_table(cnx)
        else:
            print(err)
            exit(1)
        cnx.close()


def create_table(cnx):
    teachers_table = (
        "CREATE TABLE `teachers` ("
        "`teacher_id` varchar(12) NOT NULL ,"
        "`title` enum('Dr.','Mr.','Mrs.','Ms.') NOT NULL,"
        "`first_name` varchar(14) NOT NULL,"
        "`last_name` varchar(16) NOT NULL,"
        "`gender` enum('M','F') NOT NULL,"
        "`designation` enum('Asst. Professor','Professor','Acct. Professor') NOT NULL,"
        " PRIMARY KEY (`teacher_id`)"
        ") ENGINE=InnoDB")

    attendance_table = (
        "CREATE TABLE `attendance` ("
        "`teacher_id` varchar(12) NOT NULL ,"
        "`current_date` date NOT NULL,"
        "`login_time` time NOT NULL,"
        "`logout_time` time,"
        " FOREIGN KEY (`teacher_id`) REFERENCES teachers(`teacher_id`),"
        " CONSTRAINT pk_attendance_id PRIMARY KEY (`teacher_id`,`current_date`)"
        ") ENGINE=InnoDB")
    cursor = cnx.cursor()

    tbls = [['teachers',teachers_table],['attendance',attendance_table]]

    for name, ddl in tbls:
        try:
            print"Creating table {}: ".format(name)
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print "already exists."
            else:
                print err.msg
        else:
            print "OK"
    cursor.close()

def add_teacher(teacher_id,title,first_name,last_name,gender,designation,db='RJIT'):
    cnx = connect()
    cnx.database = db
    cursor = cnx.cursor()
    add_teacher = ("INSERT INTO `teachers` "
                   "(teacher_id, title, first_name, last_name, gender ,designation)"
                   "VALUES (%s, %s, %s, %s, %s, %s)")
    data_teacher = (teacher_id,title,first_name,last_name,gender,designation)
    try:
        cursor.execute(add_teacher, data_teacher)
        cnx.commit()
        print "Teacher '{}' added to the table 'teachers'".format(first_name+" "+last_name)
    except mysql.connector.Error as err:
        print err.msg
    cursor.close()
    cnx.close()
    

def mark_attendance(cnx,tid):
    x = int(tid)
    if x < 10:
        tid = '0'+str(x)
    teacher_id = 'RJITCSEIT'+tid
    cursor = cnx.cursor()
    name = None
    try:
        cursor.execute("SELECT `first_name`, `last_name` FROM `teachers` \
                       WHERE `teacher_id` = '{}'".format(teacher_id))
        s = cursor.fetchall()
        name = s[0][0] +' '+s[0][1]
    except mysql.connector.Error as err:
        print err.msg
            
    present = True
    try:
        cursor.execute("SELECT * FROM `attendance` WHERE `teacher_id` = '{}' \
                       and `current_date` = CURRENT_DATE()".format(teacher_id))
        if not cursor.fetchall():
            present = False
    except mysql.connector.Error as err:
        print err.msg
    print present
    if not present:
        mark_attendance = ("INSERT INTO `attendance` "
                       "(`teacher_id`, `current_date`, `login_time`) \
                       VALUES ('{}', CURRENT_DATE(), CURRENT_TIME())".format(teacher_id))
        print 'Hello'
    else:
        mark_attendance = ("UPDATE `attendance` SET `logout_time` = CURRENT_TIME() \
                           WHERE `attendance`.`teacher_id` = '{}' AND \
                           `attendance`.`current_date` = CURRENT_DATE()".format(teacher_id))
        print 'HIiii'
    try:
        cursor.execute(mark_attendance)
        cnx.commit()
        print "Attendance marked for '{}'".format(name)
    except mysql.connector.Error as err:
        print err.msg
    cursor.close()
    