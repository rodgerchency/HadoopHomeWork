#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:57:42 2020

@author: rodger_chen
"""
import requests
from bs4 import BeautifulSoup
from udicOpenData.stopwords import rmsw

class QARobotIII:

    def __init__(self):
        self._maps = ['A','B','C']
        self._isReverse = False
        self._proxy = {
                'https':'https://59.124.224.180:3128',
                'http':'http://59.124.224.180:4378'
        }
        self._headers = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }

    def getMax(self, arr):
        if arr[0] > 0 or arr[1] > 0 or arr[2] > 0:
            maxIdx = None
            if self._isReverse:
                maxIdx = arr.index(min(arr))
            else:
                maxIdx = arr.index(max(arr))
            for i in range(3):
                if i == maxIdx:
                    continue
                elif arr[i] == arr[maxIdx]:
                    return None
            if self._isReverse:
                return min(arr)
            else:
                return max(arr)
        else:
            return None

    def clearQuestion(self, text):
            word = text.replace('下列何者是','')
            word = text.replace('下列何者','')
            word = word.replace('之一','')
            word = word.replace('請問','')
            word = word.replace('的呢','')
            return word

    def detectReverse(self, text):
            if '不是' in text:
                self._isReverse = True
            else:                
                self._isReverse = False

    def isRejectWord(self, text):
        if len(text) == 1:
            return True
        return text in ['一個', '一部', '一件']
        
    def solve(self, jsonQA):
        
        self.detectReverse(jsonQA['Question'])
        cnts = [0, 0, 0]
        question = self.clearQuestion(jsonQA['Question'])
        print(question)
        r = requests.get('https://www.google.com/search?q=' + question + '&#hl=zh-TW&lr=lang_zh-TW&q=%s')
        
        print(r.status_code)
        if r.status_code == requests.codes.ok:
            print('開始解析')
            # 以 BeautifulSoup 解析 HTML 程式碼
            soup = BeautifulSoup(r.text, 'html.parser')
            stories = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
            # print(jsonQA['A'], ',',jsonQA['B'], ',',jsonQA['C'], ',', )
            for s in stories:     
                # print(s.text)

                cnts[0] = cnts[0] + s.text.count(jsonQA['A'])
                cnts[1] = cnts[1] + s.text.count(jsonQA['B'])
                cnts[2] = cnts[2] + s.text.count(jsonQA['C'])
           
            print(cnts)
            maxIdx = self.getMax(cnts)
            print(maxIdx)
            if maxIdx is not None:
                return self._maps[cnts.index(maxIdx)]
        return None
    
    def solvePTT(self, jsonQA):
        self._isReverse = False
        cnts = [0, 0, 0]
        question = self.clearQuestion(jsonQA['Question'])
        words = list(rmsw(question, flag=True))
        for word in words:
            print(word[0], word[1])
            if self.isRejectWord(word[0]) or 'v' in word[1]:
                continue
            question = word[0]
            r = requests.get('https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=zh-TW&source=gcsc&gss=.com&cselibv=921554e23151c152&cx=partner-pub-6282720366794148:2717804370&q=' + question +'&safe=off&cse_tok=AJvRUv31ziuahM3HbDXk7eRPoSTK:1607061745765&exp=csqr,cc&oq='+ question + '&gs_l=partner-generic.12...0.0.3.46500.0.0.0.0.0.0.0.0..0.0.csems%2Cnrl%3D13...0.40936j1675101248j3....34.partner-generic..0.0.0.&callback=google.search.cse.api3568')
            if r.status_code == requests.codes.ok:
                soup = BeautifulSoup(r.text, 'html.parser')

                cnts[0] = cnts[0] + str(soup).count(jsonQA['A'])
                cnts[1] = cnts[1] + str(soup).count(jsonQA['B'])
                cnts[2] = cnts[2] +str(soup).count(jsonQA['C'])

        print(cnts)
        maxIdx = self.getMax(cnts)
        # print(maxIdx)
        if maxIdx is not None:
            return self._maps[cnts.index(maxIdx)]
        else:
            return None

    def solveWiki(self, jsonQA):
        _headers = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'cookie':'CGIC=IocBdGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2UvYXZpZixpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIzO3E9MC45; 1P_JAR=2020-12-04-04; NID=204=wN7wT7ib3IEaOfrU5gG0a84aJyxUD5rfWn-LmYjlasr9H0MQodVfhpdY2SrS4kCrZr-NYVbH3VRK3horBOCQl_q6aZ0Cc18keRJSj5E_PRdUjexCgRi96_8ET9rA1qx5EI-ze7Bf_lNgRCgcQmsCWVkgicvW7bHYxTKPBtaIrkM',
            'accept-language' : 'zh-TW,zh'
        }
        self._isReverse = False
        cnts = [0, 0, 0]
        question = self.clearQuestion(jsonQA['Question'])
        for i in range(3):
            idx = self._maps[i]
            question = jsonQA[idx]
            r = requests.get('https://zh.wikipedia.org/wiki/' + question, headers=_headers)
            if r.status_code == requests.codes.ok:
                soup = BeautifulSoup(r.text, 'html.parser')
                # print(soup.text)
                words = list(rmsw(question, flag=True))
                for word in words:
                    if self.isRejectWord(word[0]) or 'v' in word[1]:
                        continue
                    cnts[i] = cnts[i] + soup.text.count(word[0])

        print(cnts)
        maxIdx = self.getMax(cnts)
        # print(maxIdx)
        if maxIdx is not None:
            return self._maps[cnts.index(maxIdx)]
        else:
            return None
