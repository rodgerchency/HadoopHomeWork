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
with open(path, encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)
    
cnt =0
for article in list(objects)[0:100]:
  cnt = cnt+1
  print(cnt)
  content = article["content"].split("/")  
  for word in content:
      if word == '':
          continue
      temp = word.split()
      tword = temp[0]
      if len(temp) > 1:
          ttype = temp[1]
          if ttype == 'x' or ttype == 'v' or ttype == 'ud'\
          or ttype == 'ug' or ttype == 'uj' or ttype == 'ul'\
          or ttype == 'uv' or ttype == 'uz'\
          or ttype == 'm' or ttype == 'mg' or ttype == 'mq'\
          or ttype == 'a' or ttype == 'p' or ttype == 'c':
              continue
      else:
          continue;          
      if len(tword) == 1:
          continue
      if tword in data:
          data[tword]["cnt"] = int(data[tword]["cnt"]) + 1
          if article['id'] not in data[tword]['id']:
              data[tword]['id'].append(article['id']);              
      else:
            data[tword] = {};
            data[tword] = {
                'cnt': 1,
                'type':ttype,
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