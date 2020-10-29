# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:34:01 2020

@author: rodger
"""
import json
import ijson
import io
from QARobot import QARobot
# path = "./ignore/jsonJieba-tran.json";
# f = io.open(path, encoding="utf-8")
# objects = ijson.items(f, 'item')

# path = 'data_full.txt'
# data={}
# with io.open(path, encoding="utf-8") as jsonFile:
#     data = json.load(jsonFile)

pathQA = "./questions_example_wrong2.json"
dataQA={}
with io.open(pathQA, encoding="utf-8") as jsonFile:
    dataQA = json.load(jsonFile)

robot= QARobot()
# robot.getAnswer(dataQA[0], 0)
for i in range(len(dataQA)):
    robot.getAnswer(dataQA[i], i)

# robot.getAnswer(dataQA[0],0)
# robot.getAnswer(dataQA[1],1)
