import shelve
d=shelve.open('shelve_obj')

def sayhai(name,gae):
    print('you name %s is age %s' %(name,age))

name1={'name':'zcq','age':'24'}
name2=['shevle','trafile','time','random']

d["name"]=name1   # 持久化数据 会生成三个文件
d['test']=name2   #持久化数据 会生成三个文件