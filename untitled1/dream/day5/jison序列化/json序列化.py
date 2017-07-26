import json
data ={ 'name':'zcq','age':'23','zcq':'hha'}
f=open('data.txt','w',encoding='utf-8')
f.write(json.dumps(data))   #写入

#json.dump(data,f)       #也代表写入
#json.dump([1,2,3],f)
print(data['age'],data['name'])


#data=json.loads(f)

