#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:58:40 2019

@author: meco
"""

import sqlite3 as lit

def main():
    try:
        db = lit.connect('employee.db')
        print('Database created successfully')
    except:
        print ('failed to create database')
    finally:
        db.close()
