
import json
import ijson
import itertools  

# path = "data_full.txt"
path = "./ignore/jsonJieba-tran.json";
# path = "./ignore/WikiJson.json";
f = open(path, encoding="utf-8")
objects = ijson.items(f, 'item')
data = {}


cnt =0
for article in list(objects):
    if article['title'] == '瑞士':
        data[article['title']] = article
    elif article['title'] == '官方語言':
        data[article['title']] = article
    elif article['title'] == '英語':
        data[article['title']] = article
    elif article['title'] == '中文':
        data[article['title']] = article
    elif article['title'] == '德語':
        data[article['title']] = article
    elif article['title'] == '何仙姑':
        data[article['title']] = article
    elif article['title'] == '曹國舅':
        data[article['title']] = article
        
        
# for r in objects:
#     print(r)


# for r in objects:
#     print(r)
# result = None
# for r in objects:
#     result = r;

# print(result);
# def fun(key):
    
#     objects, copy = ijson.items(f, '海因裏希')
    
#     result = None
#     for r in copy:
#         result = r;
#     return result

# arr =  dict(ijson.items(f, ''))

# print(arr['海因裏希'])

# data = ijson.parse(open(path, 'r'))


        
# for i in list(ijson.items(f, '海因裏希')):
    
#     print(i)


# for i in ijson.items(f, '吳三桂'):
#     print(i)

# objects = ijson.items(f, '')


# parser = ijson.parse(f)
# for prefix, event, value in parser:
#     print(prefix, event, value)
# print('123')
# if objects.hasNext():
#     print('has')
# else:
#     print('not')
# for article in list(objects):
#     print(article)
