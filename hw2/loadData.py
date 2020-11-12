# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 23:31:02 2020

@author: rodge
"""

import json
import ijson

path = 'data_full.txt'
data={}
with open(path, encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)
    
    
# pathQA = "./questions_example_wrong.json"
# dataQA={}
# with open(pathQA, encoding="utf-8") as jsonFile:
#     dataQA = json.load(jsonFile)
    
#     for d in dataQA:
#         print(d['A'] , d['A'] in data)
#         print(d['B'] , d['B'] in data)
#         print(d['C'] , d['C'] in data)
    