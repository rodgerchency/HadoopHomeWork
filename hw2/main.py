# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:34:01 2020

@author: rodger
"""
import json
import ijson
import io
from QARobotII import QARobotII
from datetime import datetime
# print(datetime.now())
first_time = datetime.now()
# path = "./ignore/jsonJieba-tran.json";
# f = io.open(path, encoding="utf-8")
# objects = ijson.items(f, 'item')

# path = 'data_full.txt'
# data={}
# with io.open(path, encoding="utf-8") as jsonFile:
#     data = json.load(jsonFile)

# pathQA = "./questions_example.json"
pathQA = "./question/Questions_with_Ans.json"
dataQA={}
with io.open(pathQA, encoding="utf-8") as jsonFile:
    dataQA = json.load(jsonFile)

robot = QARobotII()
answer = []
for i in range(len(dataQA)):
    answer.append(robot.solve(dataQA[i]))
print(answer)

cnt = 0
for i in range(len(answer)):
    if answer[i] != dataQA[i]['Answer']:
        cnt = cnt + 1
        print(answer[i] , ' ', i, ' ', dataQA[i]['Question'])

print(cnt)
# robot= QARobot()
# answer = []
# for i in range(len(dataQA)):
#     answer.append(robot.getAnswer(dataQA[i], i + 1))
# print(answer)

# robot.getAnswer(dataQA[1],2)
# robot.getAnswer(dataQA[19],1)

later_time = datetime.now()
difference = later_time - first_time
print(difference.seconds)