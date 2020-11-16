#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:54:15 2020

@author: rodger_chen
"""
import io
import json
import ijson
from udicOpenData.stopwords import rmsw


class QARobotII:

    def __init__(self):
        self._maps = ['A','B','C']
        self._questionDic = {}
        self.contentDics = []
        self._dataPtt = {}
        path = 'dataPtt.txt'
        with io.open(path, encoding="utf-8") as jsonFile:
            self._dataPtt = json.load(jsonFile)
        
        for i in range(1,10):
            print(i)
            path = './data/data_Content_' + str(i) + ".txt"
            with open(path, encoding="utf-8") as jsonFile:        
                self.contentDics.append(json.load(jsonFile))
        
        path = './data/idxMapping.txt'
        self.titleMapping = {}
        with open(path, encoding="utf-8") as jsonFile:        
            self.titleMapping = json.load(jsonFile)
        # path = 'data_Content.txt'
        # with io.open(path, encoding="utf-8") as jsonFile:
        #     self._data = json.load(jsonFile)

    def checkKey(self, key, dic):
        try:
            return dic[key]
        except:
            return None
    
    def getIndex(self, val, dic):
        try:
            return dic.index(val)
        except:
            return None
        
    def popItem(self, val, dic):
        try:
            dic.pop(val)
            return 1
        except:
            return None
    def getWords(self, jsonQA):
        words = list(rmsw(jsonQA['Question'], flag=True))
        return words
        
    def getContexnt(self, idx):
        # idx = 0
        idxDic1 = idx // 100000
        idxDic2 = idx % 100000
        key = list(self.contentDics[idxDic1])[idxDic2]
        return self.contentDics[idxDic1][key]
    
    def getContentByKey(self, key):
        idxTitle = self.checkKey(key, self.titleMapping)
        print(idxTitle)
        if idxTitle is not None:
            print(self.getContexnt(idxTitle))
            return self.getContexnt(idxTitle)
        else:
            return None
        
    def getMax(self, arr):
        if arr[0] > 0 or arr[1] > 0 or arr[2] > 0:
            maxIdx = arr.index(max(arr))
            print('max ', maxIdx)
            for i in range(3):
                if i == maxIdx:
                    continue
                elif arr[i] == arr[maxIdx]:
                    return None
            return max(arr)
        else:
            return None
    def clearQuestion(self, text):
        word = text.replace('·','');
        word = word.replace('、','');
        word = word.replace('，','');
        word = word.replace('。','');
        word = word.replace('美國隊長', ' 美國隊長')
        word = word.replace('安傑薩普科夫斯基', ' 安傑薩普科夫斯基')
        word = word.replace('情境推理', ' 情境猜謎 ')
        return word
    
    def clearSelect(self, choices):
        
        ret = ['','','']
        idx = 0
        for choice in choices:
            ret[idx] = choice
            ret[idx] = ret[idx].replace('獵魔人','獵魔士');
            ret[idx] = ret[idx].replace('意大利','義大利');
            if self.checkKey(choice, self.titleMapping) is None:
                if '系列' in choice:
                    ret[idx] = ret[idx].replace('系列', '')
            idx = idx + 1
        return ret
            
    def isRejectWord(self, text):
        return text in ['一個', '一部', '一件']
    
    def solve(self, jsonQA):
        
        question = self.clearQuestion(jsonQA['Question'])
        words = list(rmsw(question, flag=True))
        choices = [jsonQA['A'], jsonQA['B'], jsonQA['C']]
        choices = self.clearSelect(choices)
        ansMethodA = self._methodA(question, jsonQA['A'], jsonQA['B'], jsonQA['C'])
        if ansMethodA is not None:
            print('solve by methodA')
            print(question)
            return ansMethodA
        cnts = [0, 0, 0]
        idx = 0
        for word in words:
            if self.isRejectWord(word[0]):
                continue
            idxTitle = self.checkKey(word[0], self.titleMapping)
            # print(idxTitle)
            if idxTitle is not None:
                val = self.getContexnt(idxTitle)
                print(word[0], '在字典裡')
                idx = 0
                for choice in choices:
                    print(choice , ',', choice in val['c'])
                    if choice in val['c']:
                        cnts[idx] = cnts[idx] + val['c'].count(choice)
                        # cnts[idx] = cnts[idx] + 1 
                        # return self._maps[idx]
                    idx = idx + 1
        ansA = [cnts[0], cnts[1], cnts[2]]
        print(ansA)
        
        print('try b')
        cnts = [0, 0, 0]
        idx = 0
        for choice in choices:
            idxTitle = self.checkKey(choice, self.titleMapping)
            print(idxTitle)
            if idxTitle is not None:
                val = self.getContexnt(idxTitle)
                if val is not None:
                    for word in words:
                        if self.isRejectWord(word[0]):
                            continue
                        # print(word[0], ',', word[0] in val['c'])
                        if word[0] in val['c']:
                            cnts[idx] = cnts[idx] + 1
            idx = idx + 1
        ansB = [cnts[0], cnts[1], cnts[2]]
        print(ansB)
        ansFinal = [ansA[0] + ansB[0], ansA[1] + ansB[1], ansA[2] + ansB[2]]
        print(ansFinal)
        maxIdx = self.getMax(ansFinal)
        print(maxIdx)
        if maxIdx is not None:
            return self._maps[ansFinal.index(maxIdx)]
        else:
            keys = self._dataPtt.keys()
            idx = 0
            for choice in choices:
                for key in list(keys):
                    if choice in self._dataPtt[key]['c']:
                        print(idx, ',', choice)
                        return self._maps[idx]
                idx = idx + 1
            # ansA = self._methodA(words, jsonQA['A'], jsonQA['B'], jsonQA['C'])
            # if ansA is not None:
            #     return ansA
            
            # return self._maps(ansFinal.index(max(ansFinal)))
            return None
            
    # 從答案和內容比較
    def _methodA(self, question, choiceA, choiceB, choiceC):
        print('***_methodA***')
        if choiceA in question and choiceB not in question and choiceC not in question:
            print(question)
            print(choiceA)
            return 'A'
        elif choiceB in question and choiceA not in question and choiceC not in question:
            return 'B'
        elif choiceC in question and choiceB not in question and choiceA not in question:
            return 'C'
        # for word in words:
        #     print(word[0], ",", word[1])
            # if len(word[0]) == 1:
            #     continue
            # if word[0] == choiceA:
            #     # print('找到',word,'和',choiceA,'相等')
            #     return 'A'
            # elif word[0] == choiceB:
            #     # print('找到',word,'和',choiceB,'相等')
            #     return 'B'
            # elif word[0] == choiceC:
            #     # print('找到',word,'和',choiceC,'相等')
            #     return 'C'
            # elif (word[0] in choiceA or choiceA in word[0]) and \
            # (word[0] not in choiceB and choiceB not in word[0]) and\
            # (word[0] not in choiceC and choiceC not in word[0]):
            #     # print(word[0] in choiceA, ',', choiceA in word[0], ',', word[0], ',',choiceA)
            #     return 'A'
            # elif (word[0] in choiceB or choiceB in word[0]) and \
            # (word[0] not in choiceA and choiceA not in word) and\
            # (word[0] not in choiceC and choiceC not in word[0]):
            #     # print(word[0] in choiceB, ',', choiceB in word[0], ',', word[0], ',',choiceB)
            #     return 'B'
            # elif (word[0] in choiceC or choiceC in word[0]) and \
            # (word[0] not in choiceA and choiceA not in word[0]) and\
            # (word[0] not in choiceB and choiceB not in word[0]):
            #     # print(word[0] in choiceC, ',', choiceC in word[0], ',', word[0], ',',choiceC)
            #     return 'C'
        return None


    def askQuestion(self, dataQA):
        cnt = 0
        # 把問題蒐集起來
        questions = []
        queryQA = []
        for i in range(len(dataQA)):
            words = list(rmsw(dataQA[i]['Question'], flag=True))
            keys = []
            for word in words:
                if len(word[0]) > 1 and 'n' in word[1]:
                    keys.append(word[0])
                    if self.checkKey(word[0], self._data) is not None:
                        if word[0] not in queryQA:
                            queryQA.append(word[0])
            questions.append(keys)
        
        querySelect = []
        for i in range(len(dataQA)):
            if self.checkKey(dataQA[i]['A'], self._data) is not None:
                querySelect.append(dataQA[i]['A'])
            
            if self.checkKey(dataQA[i]['B'], self._data) is not None:
                querySelect.append(dataQA[i]['B'])
            
            if self.checkKey(dataQA[i]['C'], self._data) is not None:
                querySelect.append(dataQA[i]['C'])
            
        self._data = None
        return queryQA, querySelect

        totalQ = len(queryQA)        
        print(totalQ)
        path = "./ignore/jsonJieba-tran.json";
        f = open(path, encoding="utf-8")
        objects = ijson.items(f, 'item')
        for article in list(objects):
            sizeQA = len(queryQA)
            print(cnt, ',', sizeQA)
            cnt = cnt + 1
            if sizeQA > 0:
                idx = self.getIndex(article['title'], queryQA);                
                if idx is not None:
                    queryQA.pop(idx)
                    self._questionDic[article['title']] = article                    
            else:
                break
                    
                    
                    
                    
                    
                    
                    
                    
        
