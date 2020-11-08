# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 14:50:50 2020

@author: rodge
"""


class StringUtil:

    def __init__(self):
        print('init')

    def setRule(self, pair1, pair2):
        #「」
        self._pair1 = pair1
        self._pair2 = pair2
        
    def _getIndex(self, word):
        try:
            return self._pair1.index(word)            
        except:
            return None

    def getSplit(self, context):

        pos = 0
        length = len(context)
        nowlook = None
        result = []
        word = ''
        while (pos < length):
            if nowlook is not None:
                # Find
                if nowlook == context[pos]:
                    result.append(word)
                # Keep finding
                else:
                    word = word + context[pos]
            else:
                idx = self._getIndex(context[pos])
                if idx is not None:
                    nowlook = self._pair2[idx]
            pos = pos + 1
        return result

