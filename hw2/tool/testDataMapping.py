#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:56:48 2020

@author: rodger_chen
"""
import json

path = '../data/idxMapping.txt'
titleMapping = {}
with open(path, encoding="utf-8") as jsonFile:        
    titleMapping = json.load(jsonFile)
        
data={}

dics = []
for i in range(1,10):
    print(i)
    path = '../data/data_Content_' + str(i) + ".txt"
    with open(path, encoding="utf-8") as jsonFile:        
        dics.append(json.load(jsonFile))

def getContent(idx):
    # idx = 0
    idxDic1 = idx // 100000
    idxDic2 = idx % 100000
    key = list(dics[idxDic1])[idxDic2]
    
    return dics[idxDic1][key]


# for key in list(titleMapping.keys()):
#     idx = titleMapping[key]
#     if key != getContent(idx):
#         print('wtf ', idx , ",",key)
#         break
print('finish')