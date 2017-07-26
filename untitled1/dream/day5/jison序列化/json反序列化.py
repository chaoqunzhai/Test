import json
f=open('data.txt',encoding='utf-8')

data= json.load(f)   #只能load一次
print(data['age'])