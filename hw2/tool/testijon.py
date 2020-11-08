
import json
import ijson
import itertools  

path = "data_full.txt"
# path = "./ignore/jsonJieba-tran.json";
f = open(path, encoding="utf-8")
# objects = ijson.items(f, '海因裏希')

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

data = ijson.parse(open(path, 'r'))


        
# for i in list(ijson.items(f, '海因裏希')):
    
#     print(i)


# for i in ijson.items(f, '吳三桂'):
#     print(i)

# objects = ijson.items(f, '')


parser = ijson.parse(f)
for prefix, event, value in parser:
    print(prefix, event, value)
# print('123')
# if objects.hasNext():
#     print('has')
# else:
#     print('not')
# for article in list(objects):
#     print(article)
