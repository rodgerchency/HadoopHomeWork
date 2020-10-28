
#encoding=utf-8
import io
import json
import jieba
jieba.set_dictionary('D:\school\HadoopHomeWork\dict.txt.big')
# sentence = "官方稱以色列國，是在位於西亞的主權國家，坐落於地中海東南岸及紅海亞喀巴灣北岸，北靠黎巴嫩，東北鄰敘利亞，東與約旦接壤，巴勒斯坦領土的約旦河西岸地區和加薩走廊各居東西，西南則為埃及。"
# print("Input：", sentence)
# words = jieba.cut(sentence, cut_all=False)
# print("Output 精確模式 Full Mode：")
# for word in words:
#     print(word)

# sentence = "官方称以色列国，是在西亚的主权国家，仅限于地中海东南岸及红海亚喀巴湾北岸，北靠立法局，东北邻叙利亚，东与约旦接壤，巴勒斯坦领土的约旦河西岸地区和加萨走廊 各居东西，西南则为埃及。"
# print("Input：", sentence)
# words = jieba.cut(sentence, cut_all=False)
# print("Output 精確模式 Full Mode：")
# for word in words:
#     print(word)
class QARobot:

    def __init__(self):
            self._data = {}
            jieba.set_dictionary('D:\school\HadoopHomeWork\dict.txt.big')
            path = 'data_full.txt'
            with io.open(path, encoding="utf-8") as jsonFile:
                self._data = json.load(jsonFile)

    def getAnswer(self, jsonQA, idx):
        words = jieba.cut(jsonQA['Question'], cut_all = False)
        ansA = self._methodA(words, jsonQA['A'], jsonQA['B'], jsonQA['C'])
        ansB = self._methodB(words, jsonQA['A'], jsonQA['B'], jsonQA['C'])
        if ansA is not None:
            print(idx, '答案是', ansA)
        # elif ansB is not None:
        else:
            print(idx, '沒有答案')
    
    # 從答案和內容比較
    def _methodA(self, words, choiceA, choiceB, choiceC):

        for word in words:
            if len(word) == 1:
                continue
            if word == choiceA:
                # print('找到',word,'和',choiceA,'相等')
                return 'A'
            elif word == choiceB:
                # print('找到',word,'和',choiceB,'相等')
                return 'B'
            elif word == choiceC:
                # print('找到',word,'和',choiceC,'相等')
                return 'C'
            elif (word in choiceA or choiceA in word) and \
            (word not in choiceB and choiceB not in word) and\
            (word not in choiceC and choiceC not in word):
                print(word in choiceA, ',', choiceA in word, ',', word, ',',choiceA)
                return 'A'
            elif (word in choiceB or choiceB in word) and \
            (word not in choiceA and choiceA not in word) and\
            (word not in choiceC and choiceC not in word):
                print(word in choiceB, ',', choiceB in word, ',', word, ',',choiceB)
                return 'B'
            elif (word in choiceC or choiceC in word) and \
            (word not in choiceA and choiceA not in word) and\
            (word not in choiceB and choiceB not in word):
                print(word in choiceC, ',', choiceC in word, ',', word, ',',choiceC)
                return 'C'

        # print('方法A沒找到')
        return None

    def _methodB(self, words, choiceA, choiceB, choiceC):
        cntA = 0        
        if choiceA in self._data:
            cntA = self._data[choiceA]['cnt']
        cntB = 0        
        if choiceB in self._data:
            cntB = self._data[choiceB]['cnt']
        cntC = 0        
        if choiceC in self._data:
            cntC = self._data[choiceC]['cnt']
        print('choiceA cnt :', cntA)
        print('choiceB cnt :', cntB)
        print('choiceC cnt :', cntC)
        return None



