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
path = '../data/data_Content_9.txt'
with open(path, encoding="utf-8") as jsonFile:        
    data = json.load(jsonFile)

# arr = []
# for key in data.keys():
#     if '峯' in data[key]['c']:
#         data[key]['c'] = data[key]['c'].replace('峯','峰')
#         # print(key)
#         # arr.append(key)

content = '簡稱伊州，是一個位於美國中西部的州，州名源自曾在此居住的伊利尼維克（Illiniwek）印第安人部落。\
「Illinois」這個名字就是法國殖民者根據此部落名稱變形而得來的。伊利諾州的州府是位於該州南部的春田（Springfield）。伊利諾州的美國郵政縮寫代碼為「IL」\
以印第安人伊利諾部落之名（Iliniwek）命名，意思是戰士。17-18世紀法國探險家沿著密西西比河溯流而上，進入伊利諾中西部開展貿易，\
並開闢了密西西比河經伊利諾河進入五大湖區的貿易通道，期間建立了皮奧里亞等定居點。此後法國將伊利諾納入新法蘭西殖民地。\
1756-1763年的七年戰爭中法國戰敗，將五大湖區和加拿大割讓給英國，但英國頒布禁止墾殖的禁令，不允許北美東岸十三殖民地的居民遷入。\
1783年巴黎條約將密西西比河以東的英國殖民地割讓與美國，其中包括伊利諾。\
1809年2月3日，伊利諾領地成立。\
1818年12月3日，伊利諾成為美國的第21個州。\
1832年4月發生黑鷹戰爭，為美國政府與美洲原住民之間的戰爭。蘇族領導者黑鷹，率領密西西比河兩岸的數個蘇族，在伊利諾州與愛荷華州一帶，與美國政府作戰。原住民部落聯軍最終遭擊敗。\
1834年林肯當選為州議員開始其政治生涯，因此該州也被稱為「林肯之地」（Land of Lincoln）\
1880-1920年間伊利諾州和芝加哥經歷了經濟發展的黃金時代，芝加哥人口迅速增長，與此同時伊利諾州多個城市成為了工業城，包括喬利埃特和羅克福德就是在這一時期成為工業區。\
1957年，芝加哥附近的阿貢國家實驗室啟動了美國的第一個實驗性核發電系統，至今有11家核電站正在運營，伊利諾伊州的核電發電量為全美第一。\
1960年，Ray Kroc在Des Plaines開設了第一家麥當勞專賣店（它仍然是一家博物館，在街對面有麥當勞）。\
1970年代開始，伊利諾州經歷了去工業化和逆城市化帶來的衰退，多個城市因為稅收銳減和市中心空心化出現了高犯罪率和高空置率的問題。其中一些城市因犯罪臭名昭著，如東聖路易斯斯和春田。'

idx = 876243
keyword = '伊利諾州'
# del data[keyword]
content = clearWord(content)
print(content)
data[keyword] = {
    'c':content
    }
# data[keyword]['c'] = content
# data[keyword]['c'] = data[keyword]['c'] + content

with open(path, 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)



pathTitle = '../data/idxMapping.txt'
titleData={}
with open(pathTitle, encoding="utf-8") as jsonFile:
    titleData = json.load(jsonFile)

titleData[keyword] = idx
with open(pathTitle, 'w', encoding='utf-8') as outfile:
    json.dump(titleData, outfile, ensure_ascii=False)

        