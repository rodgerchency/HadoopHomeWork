# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:00:25 2020

@author: rodger
"""

import json
import ijson
import re

path = "../ignore/jsonJieba-tran.json";
f = open(path, encoding="utf-8")
objects = ijson.items(f, 'item')

path = '../data/data.txt'
data={}
with open(path, encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)


def clearWord(word, keyWord):
    
    r1 = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
    # word = word.replace('-','')
    # word = word.replace('，','')
    # word = word.replace('。','')
    keyword1 = keyWord.replace('-','')
    keyword2 = keyWord.replace('·','')
    word = word.replace('；','')
    word = word.replace('·','')
    word = word.replace('：','')
    word = word.replace('（','')
    word = word.replace('）','')
    word = word.replace('「','')
    word = word.replace('」','')
    word = word.replace(keyWord,'')
    word = word.replace(keyword1,'')
    word = word.replace(keyword2,'')
    return re.sub(r1, '', word)
    # return word

cnt =0
for article in list(objects)[800000:]:
  cnt = cnt+1
  # print(article["content"])
  
  print(cnt)
  content = article["content"].split("/") 
  textContent = ''
  for word in content:
      if word == '':
          continue
      temp = word.split()
      textContent = textContent + temp[0]      
      textContent = clearWord(textContent, article['title'])
      # if len(textContent) >= 100:
      #     break  
  if article['title'] not in data:
    data[article['title']] = {}
    data[article['title']] ={
        'c':textContent
    }
  else:
      print(article['title'] + " has exist")
  
  
with open(path, 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)
