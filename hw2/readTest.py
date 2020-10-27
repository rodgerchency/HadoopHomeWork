# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 16:10:23 2020

@author: rodge
"""
import json
import re
# try:
#     # f = open('/ignore/jsonJieba-tran.json', 'r')
#     f = open('/ignore/test.txt', 'r')
#     print(f.read());
# finally:
#     f.close()

filename = "./ignore/jsonJieba-tran.json"
# filename = "./ignore/test.txt"

jsons = [];
temps = []
with open(filename,"r", encoding="utf-8") as f:
    cnt = 0
    for fLine in f:
        # print(cnt)
        # print(fLine)
        print(type(fLine))        
        strs = fLine.split('{');
        size = len(strs);
        for i in range(1 ,size):
            print(i, ",", cnt)
            cnt = cnt + 1
            if strs[i][len(strs[i]) - 1] == '}':
                if len(temps) == 0:
                    if i == size -1:                
                        jsons.append(json.loads("{" + strs[i][0:len(strs[i]) - 2]))
                    else:                
                        jsons.append(json.loads("{" + strs[i][0:len(strs[i]) - 1]))
                else:
                    temps.append(strs[i])
                    temp = ''.join(temps)
                    jsons.append(json.loads("{" + temp))
            else:
                temps.append(strs[i])