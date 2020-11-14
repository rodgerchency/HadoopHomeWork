#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:32:07 2020

@author: rodger_chen
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:00:25 2020

@author: rodger
"""

import json
import ijson
import re


path = '../data/idxMapping.txt'
data={}
with open(path, encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)


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
    print(idxDic1 , ",", idxDic2)
    try:
        return list(dics[idxDic1])[idxDic2]
    except:
        print(idxDic1 , ",", idxDic2)
        return None

    
cnt = 0
while(cnt < 876240):
    key = getContent(cnt)
    if key is not None:
        newKey = key.replace('·','');
        data[newKey] = cnt
    cnt = cnt + 1
    
    
    


# cnt =0
# for article in list(objects):
  
#   print(cnt)
#   # content = article["content"].split("/") 
#   textContent = ''
#   # for word in content:
#   #     if word == '':
#   #         continue
#   #     temp = word.split()
#   #     textContent = textContent + temp[0]      
#   #     textContent = clearWord(textContent, article['title'])
#   #     # if len(textContent) >= 100:
#   #     #     break  
#   if article['title'] not in data:
#     data[article['title']] = {}
#     data[article['title']] = cnt
#   else:
#       print(article['title'] + " has exist")
#   cnt = cnt+1
  

path = '../data/idxMapping.txt'
with open(path, 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)
print('finish')
