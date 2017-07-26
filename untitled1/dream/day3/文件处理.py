#print(open('ceshi').read())
# w 创建写模式 ,覆盖
#a 追加模式
# r  默认为读模式
#r+ ： 读写
#w+ ： 写读
#a+ ： 追加读

f=open('字符编码',encoding='utf-8')
print(f.readline())
print(type(f))
#f.truncate(100) # 截断范围 (开头数100个数字)
