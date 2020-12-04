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

    def getMax(self, arr):
        if arr[0] > 0 or arr[1] > 0 or arr[2] > 0:
            maxIdx = None
            if self._isReverse:
                maxIdx = arr.index(min(arr))
            else:
                maxIdx = arr.index(max(arr))
            print('max ', maxIdx)
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
        print(jsonQA['Question'])
        cnts = [0, 0, 0]
        question = self.clearQuestion(jsonQA['Question'])
        r = requests.get('https://www.google.com/search?q=' + question + '&source=lnt&tbs=lr:lang_1zh-TW&lr=lang_zh-TW')
        if r.status_code == requests.codes.ok:
            # 以 BeautifulSoup 解析 HTML 程式碼
            soup = BeautifulSoup(r.text, 'html.parser')
            stories = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
            for s in stories:     
                # print(s.text)
                cnts[0] = cnts[0] + s.text.count(jsonQA['A'])
                cnts[1] = cnts[1] + s.text.count(jsonQA['B'])
                cnts[2] = cnts[2] + s.text.count(jsonQA['C'])
           
            print(cnts)
            maxIdx = self.getMax(cnts)
            # print(maxIdx)
            if maxIdx is not None:
                return self._maps[cnts.index(maxIdx)]
            else:
                return None
                print('try plan b')
                cnts = [0, 0, 0]
                for i in range(3):
                    idx = self._maps[i]
                    print('idx ', idx, ' ', i, jsonQA[idx])
                    r = requests.get('https://www.google.com/search?q=' +jsonQA[idx] + '&source=lnt&tbs=lr:lang_1zh-TW&lr=lang_zh-TW')
                    if r.status_code == requests.codes.ok:
                        stories = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
                        for s in stories:
                            words = list(rmsw(question, flag=True))
                            for word in words:
                                if self.isRejectWord(word[0]):
                                    continue
                                temp = s.text.count(word[0])
                                if temp >= 1:
                                    print(s.text)
                                    print(word[0])
                                    print(temp)
                                cnts[i] = cnts[i] + temp
                    else:
                        print(r.status_code)
                print(cnts)
                maxIdx = self.getMax(cnts)
                # print(maxIdx)
                if maxIdx is not None:
                    return self._maps[cnts.index(maxIdx)]
                else:
                    return None

                
        print(r.status_code)
        return None