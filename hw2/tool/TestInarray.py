# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 21:02:58 2020

@author: rodge
"""
import json

# json 的資料形式字串
x =  '{ "name":"jim", "age":25, "city":"Taiwan"}'

# 轉換json
person = json.loads(x)

d = {1:10,2:20}
# try:
#     t = d[11]
#     print(t)
# except:
#     print('abc')
#     print(NameError)
    
def check(key):
    try:
        t = d[key]
        return t
    except:
        return None

print(check(1))
print(check(2))
print(check(3))
print(check(4))
    