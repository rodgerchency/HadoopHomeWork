#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 09:34:16 2020

@author: rodger_chen
"""

import json
import io
import re


def clearWord(word):
    
    r1 = '[’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
    # word = word.replace('-','')
    # word = word.replace('，','')
    # word = word.replace('。','')
    word = word.replace('；','')
    word = word.replace('·','')
    word = word.replace('：','')
    word = word.replace('（','')
    word = word.replace('）','')
    word = word.replace('「','')
    word = word.replace('」','')
    word = word.replace(' ','')
    return re.sub(r1, '', word)

data = {}
path = '../data/data_Content_1.txt'
with open(path, encoding="utf-8") as jsonFile:        
    data = json.load(jsonFile)

# arr = []
# for key in data.keys():
#     if '峯' in data[key]['c']:
#         data[key]['c'] = data[key]['c'].replace('峯','峰')
#         # print(key)
#         # arr.append(key)

content = '聖母峰：8,844.43米 干城章嘉峰：8,586米 洛子峰：8,516米 馬卡魯峰：8,485米 卓奧友峰：8,188米 道拉吉里峰：8,167米\
馬納斯盧峰：8,163米 南迦帕爾巴特峰：8,125米 安納布爾納峰：8,091米 希夏邦馬峰：8,027米 格重康峰'

# idx = 876242
keyword = '喜馬拉雅山脈'
# del data[keyword]
content = clearWord(content)
print(content)
# data[keyword] = {
#     'c':content
#     }
# data[keyword]['c'] = content
data[keyword]['c'] = data[keyword]['c'] + content

with open(path, 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)



# pathTitle = '../data/idxMapping.txt'
# titleData={}
# with open(pathTitle, encoding="utf-8") as jsonFile:
#     titleData = json.load(jsonFile)

# titleData[keyword] = idx
# with open(pathTitle, 'w', encoding='utf-8') as outfile:
#     json.dump(titleData, outfile, ensure_ascii=False)

        