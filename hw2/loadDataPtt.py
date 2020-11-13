# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 11:09:54 2020

@author: rodger
"""

import json
import ijson
import jieba
import jieba.posseg as pseg


jieba.set_dictionary('D:\school\HadoopHomeWork\dict.txt.big')
pathPtt = 'dataPtt.txt'
dataPtt={}
with open(pathPtt, encoding="utf-8") as jsonFile:
    dataPtt = json.load(jsonFile)

path = 'data.txt'
data={}
with open(path, encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)

keys = dataPtt.keys()
jieba.enable_paddle()

context = '鬼滅之刃我妻善逸中文配音員江志倫。（圖／翻攝自Facebook／江志倫-牛奶）'
words = pseg.cut(context,use_paddle=True)
# for word, flag in words:
#     # if flag == 'nr' or flag == 'PER':
#     print(word, flag)
for i in list(keys)[0:10]:
    print(dataPtt[i]['c'])
    # words = pseg.cut(dataPtt[i]['c'])
    # for word, flag in words:
    #     if flag == 'nr' or flag == 'PER':
    #         print(word)
        # print('%s %s'%(word, flag))

# with open('data.txt', 'w', encoding='utf-8') as outfile:
#     json.dump(data, outfile, ensure_ascii=False)