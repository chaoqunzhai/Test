# 集合{}
# 集合的特点是去重
#2个集合的交际 用的&
#并集 用的|
#s1={1,2,3}
#s2={1,2,3,4,5,6,6,6}
# print(s2)
# print(s1|s2)
# # 差集
# print(s2-s1)
# #交集
# print(s1&s2)
# #对称差集
# print(s1^s2)
# #判断为子集,父集
# print(s1<=s2)
#print(s1>=s2)
#列表转集合
#s1=set(['c','b',1,1,2,3,4,5])
# print(s1)
# #print(s1)
# #增加集合
# s1.update('zcq')   #拆开字母增加
# print(s1)
# s2={'h','d','q'}
# s1.update(s2)
# print(s1)
# #增加 整个字符串增加
# s1.add('zhaichaoqun')
# print(s1)
# #随机删除
# #s1.pop()
# #指定删除
# s1.remove('zhaichaoqun')
# print(s1)
# 不报错的删除, 如果删除的值 不存在 也不会报错  。
# s1.discard('c')
# print(s1)
#差集更新
s1={1,2,3,4,5}
s2={1,2,3}
print(s1.difference_update(s2))  #s3=s1-s2
print(2**16)
元组是只读列表 ，例如：用来存放身份证信息 不可修改   元组是<>