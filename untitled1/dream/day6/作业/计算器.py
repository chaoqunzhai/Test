import re
obj = re.match('\d','123abcdef')       #从起始位置开始匹配
obj1 = re.search('\d+','123abcdef')     #根据模型去字符串中匹配指定内容，匹配单个
if obj:
    print('1:',obj.group())
if obj1:
    print('2:',obj1.group())

a = "1231abc456"
print('3:',re.search("([0-9]*)([a-z]*)([0-9]*)", a).group())

print('4:',re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(1))
print('5:',re.search("([0-9]*)([a-z]*)([0-9]*)", a).groups())

obj2 = re.findall('\d+', 'fa123+1uu888asf')       #匹配字符串中所有的符合条件的元素
print('6:',obj2)

con='abc123+1+good!*22'
new_con=re.sub('\d+',' ',con)
#new_con=re.findall('\d',con)           #替换匹配字符串
print('7:',new_con)



content = "'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"
new1_content=re.split('\*',content)
print('8:',new1_content)

new2_content = re.split('[\+\-\*\/]+', content)
print('9:',new2_content)

content=re.sub('\s*','',content)
new3_content=re.split('\(([\+\-\*\/]?\d+[\+\-\*\/]?\d+){1}\)', content, 1)
print(new3_content)

add= "'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"
conten = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',add ).group()
print('10',conten)


acc=re.search(r"\(.+\)",add).group()
print(acc)