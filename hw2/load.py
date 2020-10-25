# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 22:14:19 2020

@author: rodger
"""
import json
import ijson

path = "./ignore/jsonJieba-tran.json";
f = open(path, encoding="utf-8")
objects = ijson.items(f, 'item')

path = 'data.txt'
data={}
with open(path) as jsonFile:
    data = json.load(jsonFile)
    
cnt =0;
for article in list(objects):
  cnt = cnt+1
  print(cnt)
  content = article["content"].split("/")  
  for word in content:
      if word == '':
          continue;
      temp = word.split()
      tword = temp[0]
      if tword in data:
          data[tword]["cnt"] = int(data[tword]["cnt"]) + 1
          if article['id'] not in data[tword]['id']:
              data[tword]['id'].append(article['id']);              
      else:
           data[tword] = {};
           data[tword] = {
               'cnt': 1,
               'id' : [article['id']]
               };
          
  # name = article['title']
  # data[name]=[]
  # data[name].append({
  #     "id":article["id"],
  #     "word":"test"
  #     });
  # print(article["id"]),
  # print(article["title"]),
  # print(article["content"])
  
with open('data.txt', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)