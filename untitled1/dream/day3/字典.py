import copy
#dic={'name':{'cq':23},'age':22}
#print(dic.get('namesasasa'))
#dic['zcq']='good'
#print(dic['name']['cq'])
#dic['name']='hahaha'
#print(dic)
#del dic['name']
#print(dic)
#浅copy只复制一层  第二层数据还是用的同一个内存地址
##深copy 完全克隆
#zidian4=
#列表l=[]
# 元祖l=（），与列表完全一致，唯一不同的是元祖内元素不可变  是以逗号为分割
#字典={}
# 用id来测试是否可变 （id来测试在内存中的地址）如果测试ID都是一样，那属于可变  测试ID不一样，属于不可以变
#key的定义规则：
# 1.不可变：数字，字符串，元祖 （可变：列表，字典）
# 2.key是唯一的 不可变的
#value定义规则：任意类型
# 字典中定义什么样 你取的时候就写什么样
#2.
# zidian={
#     'name':{'haha':'good'},
#     (1047,738527):'qq',
#     'rch':'love',
#     1: 'money',
#     'cesh':'111'
# }
# print(zidian['name']['haha'])
# print(zidian.get('name').get('haha'))
# print(zidian[1])
# print(zidian[(1047,738527)])
#zidian.clear()
#print(zidian)
# print(zidian.items())
# print(zidian.keys())
# for i in zidian.items():
#     print(i)
# for k,v in zidian.items():
#     print(k,v)
# for i in zidian.keys():
#     print(i,zidian[i])
# zidian2=dict.fromkeys('zcq',1)
# zidian2=dict.fromkeys([1,2,3],'zcq')
# print(zidian2)
# zidian.setdefault('111111',[])  # 增加值
# print(zidian)
# zidian3={'ahhahaha':'111111'}
# zidian.update(zidian3)
# print(zidian)
# print(zidian.values())
zcq={
    'name':'翟超群',
    'qq':1047738527,
    'moeny':{'信用卡':'30000','余额':'30000'}
}
rch=zcq.copy()
rch['name']='CH'
rch['qq']='800929'
print(rch)
# print(zcq)
#print(rch)
for i in zcq:
    print(i,zcq[i])
    #for e in zcq[i]:
        #print(e)