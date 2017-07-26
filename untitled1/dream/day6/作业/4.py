import re
a='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
value=re.search(r'\([^()]+\)',a).group()
# print(value)
#print(type(value))

def plus(value):
    value =value .replace(" ","")
    value =value .replace("+-","-")
    value =value  .replace("--","+")
    return value

def dive():
    while True:
        avalue = re.search(r'\([^()]+\)', a).group()
        avalue_1 = value[:i]
        avalue_2 = value[i + 1:]
        if "(" in avalue_1 and ")" in avalue_2:
            avalue_3 = avalue_1.strip("(")
            #print(avalue_3)
            avalue_4 = avalue_2.strip(")")
            #print(avalue_4)
            if "/" in value:
                avalue_5 = int(avalue_3) / int(avalue_4)
            avalue_5 = str(avalue_5)
            new_a = re.sub(value, avalue_5, a)
            print('第一次计算值:',new_a)
            #mch=re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',new_a).group()
            before, nothing, after = re.split('\(([\+\-\*\/]*\d+\.*\d*)\)', new_a,2)
            new_b=before+nothing+after
            #print('2:',new_b)
            new_c=re.search(r'\([^()]+\)', new_b).group()
            print('3:',new_c)
            new_d=re.split(r'\+',new_c)
            #print(new_d[0].strip())
            print(new_d)
            if len(new_d) >1:
                if "(" in new_d[0]:
                    new_d_1=new_d[0].strip("(")
                    print(new_d_1)
                    if "/" in new_d_1:
                        print('4:',new_d_1.index('/'))
                    if "*" in new_d_1:
                        print('5:',new_d_1.index('*'))





            break
for i,j in enumerate(value):
    if j == "*":
        break
    if j == "/":
        dive()
        break
