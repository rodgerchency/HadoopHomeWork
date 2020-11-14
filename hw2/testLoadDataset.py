#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:06:44 2020

@author: rodger_chen
"""


import json
import ijson
import io

path = "data.txt";
f = io.open(path, encoding="utf-8")
objects = ijson.items(f, 'item')
for article in list(objects):
    print(article)

