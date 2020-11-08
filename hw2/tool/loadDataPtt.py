# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 11:09:54 2020

@author: rodger
"""

import json
import ijson
import jieba
import jieba.posseg as pseg
import re
from StringUtil import StringUtil

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


strUtil= StringUtil()

# context = '鬼滅之刃我妻善逸中文配音員江志倫。（圖／翻攝自Facebook／江志倫-牛奶）'
# words = pseg.cut(context,use_paddle=True)
# for word, flag in words:
#     # if flag == 'nr' or flag == 'PER':
#     print(word, flag)
def addCell(key):
    length = len(key)
    if length > 1 and length <=6:
            if key in data:
                data[key]['cnt'] = data[key]['cnt'] + 1
            else:
                data[key] = {
                    'cnt' : 1
                }

for i in list(keys):
    
    # strUtil.setRule(['「'], ['」'])
    # results = strUtil.getSplit(dataPtt[i]['c'])
    # for result in results:
    #     addCell(result)
    
    # strUtil.setRule(['《'], ['》'])
    # results = strUtil.getSplit(dataPtt[i]['c'])
    # for result in results:
    #     addCell(result)

    # strUtil.setRule(['（'], ['）'])
    # results = strUtil.getSplit(dataPtt[i]['c'])
    # for result in results:
    #     addCell(result)
    


    # result = re.search(r"(?<=「).*?(?=」)", dataPtt[i]['c']).group(0)
    # print(result)
    # print(dataPtt[i]['c'])
    # strs = dataPtt[i]['c'].split('4.完整新聞內文:')
    # if len(strs) > 1:
    #     strs2 = strs[1].split('5.完整新聞連結')
    #     if len(strs2) > 1:
    #         print(strs2[0])
    #         data[i] = {
    #             'c' :strs2[0]
    #         }
    #     else:
    #         data[i] = {
    #             'c' :strs2[0]
    #         }

    # else:
    #     data[i]= {
    #         'c' :dataPtt[i]['c']
    #     }


    # words = pseg.cut(dataPtt[i]['c'])
    # for word, flag in words:
    #     if flag == 'nr' or flag == 'PER':
    #         print(word)
        # print('%s %s'%(word, flag))

with open('data.txt', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)
