#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:04:50 2020

@author: rodger_chen
"""

import json
import ijson
import io

path = "./ignore/jsonJieba-tran.json";
f = io.open(path, encoding="utf-8")
objects = ijson.items(f, 'item')

path = 'data.txt'
data={}
with io.open(path, encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)