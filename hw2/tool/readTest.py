# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 16:10:23 2020

@author: rodge
"""
import json
import io
# try:
#     # f = open('/ignore/jsonJieba-tran.json', 'r')
#     f = open('/ignore/test.txt', 'r')
#     print(f.read());
# finally:
#     f.close()

path = 'data_Content.txt'
dataContent = {}
with io.open(path, encoding="utf-8") as jsonFile:
  dataContent = json.load(jsonFile)