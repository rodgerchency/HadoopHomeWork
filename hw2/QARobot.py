
#encoding=utf-8
import io
import json
import jieba
import jieba.posseg as pseg

class QARobot:

    def __init__(self):
            self._data = {}
            jieba.set_dictionary('D:\school\HadoopHomeWork\dict.txt.big')
            path = 'data_full.txt'
            with io.open(path, encoding="utf-8") as jsonFile:
                self._data = json.load(jsonFile)

    def getAnswer(self, jsonQA, idx):
        # words = jieba.cut(jsonQA['Question'], cut_all = False)
        words = pseg.cut(jsonQA['Question'])
        # ansA = self._methodA(words, jsonQA['A'], jsonQA['B'], jsonQA['C'])
        ansB = self._methodB(words, [jsonQA['A'], jsonQA['B'], jsonQA['C']])
        ansC = self._methodC(words, [jsonQA['A'], jsonQA['B'], jsonQA['C']])
        # if ansA is not None:
        #     print(idx, '答案是', ansA)
        # # elif ansB is not None:
        # else:
        #     print(idx, '沒有答案')
    
    # 從答案和內容比較
    def _methodA(self, words, choiceA, choiceB, choiceC):

        print('***_methodA***')
        for word in words:
            print(word.word, ",", word.flag)
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

        # print('方法A沒找到')
        return None

    def _methodB(self, words, choices):
        
        print('***_methodB***')
        cnts = [0, 0, 0]
        idx = 0
        for choice in choices:
            if choice in self._data:
                cnts[idx] = self._data[choice]['cnt']
            print(idx , "cnt:", cnts[idx])
            idx = idx + 1
        return None

    def _methodC(self, words, choices):
        
        print('***_methodC***')
        cnts = [0, 0, 0]
        idx = 0
        for word in words:
            if len(word.word) > 1:
                if word.word in self._data:
                    idx = 0
                    for choice in choices:
                        if choice in self._data:
                            cnts[idx] = cnts[idx] + self.getConnection(choice, word.word)
                        idx = idx + 1
        print("A:", cnts[0], ",B:", cnts[1], ",C:", cnts[2])
        
    def getConnection(self, choice, word):
        cnt = 0
        for id in self._data[choice]['id']:
            if id in self._data[word]['id']:
                cnt = cnt + 1
        return cnt
    




