#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:02:45 2019

@author: meco
"""

import sqlite3 as lit

def main():
    try:
        db = lit.connect('employee.db')
        cur = db.cursor()

        tablequery = 'CREATE TABLE users (id INT, name TEXT, email TEXT'
        cur.execute(tablequery)
        print('tablequery created successfully')
    except:
        print('Unable to create table')
    finally:
        db.close()