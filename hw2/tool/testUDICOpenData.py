#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 10:40:51 2020

@author: rodger_chen
"""

from udicOpenData.stopwords import *
doc = '聖海倫火山位於下列哪個國家?'
t =list(rmsw(doc, flag=True))