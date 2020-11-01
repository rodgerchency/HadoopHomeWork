# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 09:48:16 2020

@author: rodger
"""

import requests;
from bs4 import BeautifulSoup;

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
res = requests.get(url,cookies={'over18': '1'})

print(res)
soup = BeautifulSoup(res.text,'lxml')
tmp = soup.select('.wide')[1]['href']
totalpage = int(tmp[tmp.find('index') + 5 : tmp.find('.html')]) + 1

print(totalpage)
innerRes = requests.get('https://www.ptt.cc/bbs/Gossiping/M.1604208274.A.FB4.html', cookies={'over18':'1'})
innerSoup = BeautifulSoup(innerRes.text,'html.parser')

while (1):
    for ele in soup.select('.title a'):
        innerRes = requests.get('https://www.ptt.cc' + ele['href'], cookies={'over18':'1'})
        innerSoup = BeautifulSoup(innerRes.text,'html.parser')
        print(innerRes.url)
        if '[新聞]' not in str(ele) and 'RE:' in str(ele):
            continue        
        # print(ele)
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
            tag = p.find("span", class_ = "push-tag").text
            if "推" in tag:
                score = score+1
            if "噓" in tag:
                score = score-1
            #因為該拿的都拿了，所以
            p.extract()        
        # print("計算的分數",score)
        
        print("文章內容", innerSoup.text)
        
        if totalpage - 1 == 0:
            break
        else:
            totalpage -= 1