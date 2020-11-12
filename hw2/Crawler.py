# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 09:48:16 2020

@author: rodger
"""

import requests;
from bs4 import BeautifulSoup;


import json

path = 'data.txt'
data={}
with open(path, encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
res = requests.get(url,cookies={'over18': '1'})

print(res)
soup = BeautifulSoup(res.text,'lxml')
tmp = soup.select('.wide')[1]['href']
totalpage = int(tmp[tmp.find('index') + 5 : tmp.find('.html')]) + 1

# print(totalpage)
# innerRes = requests.get('https://www.ptt.cc/bbs/Gossiping/M.1604208274.A.FB4.html', cookies={'over18':'1'})
# innerSoup = BeautifulSoup(innerRes.text,'html.parser')

cnt = 0
# totalpage=39454
# 186, 316, 391
idx = 548
while (idx <= totalpage):
    
    if idx != 0:
        url = 'https://www.ptt.cc/bbs/Gossiping/index' + str(totalpage - idx)  +'.html'
    res = requests.get(url,cookies={'over18': '1'})
    soup = BeautifulSoup(res.text,'lxml')
    print('idx ', idx)
    for ele in soup.select('.title a'):
        innerRes = requests.get('https://www.ptt.cc' + ele['href'], cookies={'over18':'1'})
        innerSoup = BeautifulSoup(innerRes.text,'html.parser')
        # print(innerRes.url)
        if '[新聞]' not in str(ele) or 'RE:' in str(ele) or 'Re:' in str(ele):
            continue
        print('cnt ' ,cnt)
        cnt = cnt + 1
        ms = innerSoup.find_all("div", class_="article-metaline")
        #print(ms)
        #扣掉 作者、標題、時間
        for m in ms:
            m.extract()
        #扣掉看板
        ms1 = innerSoup.find_all("div", class_="article-metaline-right")
        for m in ms1:
            m.extract()
        # print(innerSoup.text)
        #計算推文的分數
        pushes = innerSoup.find_all("div", class_ = "push")
        score = 0
        for p in pushes:
            # tag = p.find("span", class_ = "push-tag")
            # if type(tag) == 'NoneType':
            #     print('tag is NoneType')
            #     continue;
            # if "推" in tag.text:
            #     score = score+1
            # if "噓" in tag.text:
            #     score = score-1
            #因為該拿的都拿了，所以
            p.extract()        
        # print("計算的分數",score)
        
        # print("文章內容", innerSoup.text)
        # print(ele.string)
        data[ele.string] = {}
        data[ele.string] = {
                'c':innerSoup.text
            }
        with open('data.txt', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False)
            
        if totalpage - 1 == 0:
            break
        else:
            totalpage -= 1
    idx = idx + 1
        

with open('data.txt', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)