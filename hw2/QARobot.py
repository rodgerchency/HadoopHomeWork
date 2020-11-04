
#encoding=utf-8
import io
import json
import jieba
import jieba.posseg as pseg
import itertools  

class QARobot:

    def __init__(self):
            self._maps = ['A','B','C']
            # self._data = {}
            jieba.set_dictionary('D:\school\HadoopHomeWork\dict.txt.big')
            path = 'data_full.txt'
            with io.open(path, encoding="utf-8") as jsonFile:
                self._data = json.load(jsonFile)
                self._dataKeys = self._data.keys()
            path = 'data_Content.txt'
            with io.open(path, encoding="utf-8") as jsonFile:
                self._dataContent = json.load(jsonFile)

    def checkKey(self, key, dic):
        try:
            return dic[key]
        except:
            return None

    def getAnswer(self, jsonQA, idx):
        # words = jieba.cut(jsonQA['Question'], cut_all = False)
        words, wordsCopy = itertools.tee(pseg.cut(jsonQA['Question']))
        print('Quesion ', idx)
        ansA = self._methodA(words, jsonQA['A'], jsonQA['B'], jsonQA['C'])
        # ansB = self._methodB([jsonQA['A'], jsonQA['B'], jsonQA['C']])
        # ansC = self._methodC(wordsCopy, [jsonQA['A'], jsonQA['B'], jsonQA['C']])
        # ansD = self._methodD(jsonQA['Question'], [jsonQA['A'], jsonQA['B'], jsonQA['C']])
        

        if ansA is not None:
            return ansA
        else:
            ansD = self._methodD(jsonQA['Question'], [jsonQA['A'], jsonQA['B'], jsonQA['C']])
            if ansD is not None:
                return ansD
            else:
                ansC = self._methodC(wordsCopy, [jsonQA['A'], jsonQA['B'], jsonQA['C']])
                if ansC is not None:
                    return ansC                
                else:
                    ansB = self._methodB([jsonQA['A'], jsonQA['B'], jsonQA['C']])
                    if ansB is not None:
                        return ansB
                    else:
                        return 'D'

        # if ansD is not None:
        #     # print(idx, '答案是', ansA)
        #     return ansD
        # # elif ansB is not None:
        # else:
        #     return 'D'
        #     # print(idx, '沒有答案')
    
        
    # 從答案和內容比較
    def _methodA(self, words, choiceA, choiceB, choiceC):
        return None
        print('***_methodA***')
        for word in words:
            # print(word.word, ",", word.flag)
            if len(word.word) == 1:
                continue
            if word.word == choiceA:
                # print('找到',word,'和',choiceA,'相等')
                return 'A'
            elif word.word == choiceB:
                # print('找到',word,'和',choiceB,'相等')
                return 'B'
            elif word.word == choiceC:
                # print('找到',word,'和',choiceC,'相等')
                return 'C'
            elif (word.word in choiceA or choiceA in word.word) and \
            (word.word not in choiceB and choiceB not in word.word) and\
            (word.word not in choiceC and choiceC not in word.word):
                print(word.word in choiceA, ',', choiceA in word.word, ',', word.word, ',',choiceA)
                return 'A'
            elif (word.word in choiceB or choiceB in word.word) and \
            (word.word not in choiceA and choiceA not in word) and\
            (word.word not in choiceC and choiceC not in word.word):
                print(word.word in choiceB, ',', choiceB in word.word, ',', word.word, ',',choiceB)
                return 'B'
            elif (word.word in choiceC or choiceC in word.word) and \
            (word.word not in choiceA and choiceA not in word.word) and\
            (word.word not in choiceB and choiceB not in word.word):
                print(word.word in choiceC, ',', choiceC in word.word, ',', word.word, ',',choiceC)
                return 'C'
        return None

    def _methodB(self, choices):
        
        print('***_methodB***')
        cnts = [0, 0, 0]
        idx = 0
        for choice in choices:
            if choice in self._data:
                cnts[idx] = self._data[choice]['cnt']
            print(idx , "cnt:", cnts[idx])
            idx = idx + 1
        ans = [cnts[0], cnts[1], cnts[2]]
        print(ans)
        if cnts[0] > 0 or cnts[1] > 0 or cnts[2] > 0:
            return self._maps[ans.index(max(ans))]       
        else:
            return None

    def _methodC(self, words, choices):
        
        print('***_methodC***')
        cnts = [0, 0, 0]
        lens = [1, 1, 1]
        idx = 0
        for word in words:
            print(word.word, ',', word.flag)
            if len(word.word) > 1:
                wordVal = self.checkKey(word.word, self._data)
                if wordVal is not None:
                    idx = 0
                    for choice in choices:
                        choiceVal = self.checkKey(choice, self._data)
                        if choiceVal is not None:
                            if lens[idx] == 1:
                                lens[idx] = len(choiceVal['id'])
                            cnts[idx] = cnts[idx] + (self.getConnection(choiceVal, wordVal)/ lens[idx])
                        idx = idx + 1
                   
        ans = [cnts[0], cnts[1], cnts[2]]
        print(ans)
        if cnts[0] > 0 or cnts[1] > 0 or cnts[2] > 0:
            return self._maps[ans.index(max(ans))]       
        else:
            return None
        
    
    def _methodD(self, question, choices):
        print('***_methodD***')
        strs1= question.split('、')
        strs2= question.split('，')
        strs3= question.split('。')
        idx = 0
        for choice in choices:
            if choice in self._dataContent:
                # print(strs1[0])
                # print(strs2[0])
                # print(strs3[0])
                if strs1[0] != '' and strs1[0] in self._dataContent[choice]['c']:
                    print(choice, strs1[0],",",self._dataContent[choice]['c'])
                    return self._maps[idx]
                elif len(strs1) > 2 and strs1[1] in self._dataContent[choice]['c']:
                    print(choice, strs1[1],",",self._dataContent[choice]['c'])
                    return self._maps[idx]             
                elif strs2[0] != '' and strs2[0] in self._dataContent[choice]['c']:
                    print(choice, strs2[0],",",self._dataContent[choice]['c'])
                    return self._maps[idx]
                elif len(strs2) > 2 and strs2[1] in self._dataContent[choice]['c']:
                    print(choice, strs2[1],",",self._dataContent[choice]['c'])
                    return self._maps[idx]        
                elif strs3[0] != '' and strs3[0] in self._dataContent[choice]['c']:
                    print(choice, strs3[0],",",self._dataContent[choice]['c'])
                    return self._maps[idx]
                elif len(strs3) > 2 and strs3[1] in self._dataContent[choice]['c']:
                    print(choice, strs3[0],",",self._dataContent[choice]['c'])
                    return self._maps[idx]
            idx = idx + 1
        return None
                
    def getConnection(self, choice, word):
        cnt = 0
        for id in choice['id']:
            val = self.checkKey(id, word['id'])
            if val is not None:
                cnt = cnt + 1
            # if id in word['id']:
            #     cnt = cnt + 1
        return cnt    

    
   



