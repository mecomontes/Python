#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:14:18 2019

@author: meco
"""

from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return 'Home page'

@app.route('/about')
def about():
    return 'About page'

if __name__ == '__main__':
    app.run()