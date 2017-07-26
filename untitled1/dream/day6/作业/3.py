import re
a='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
a=a.replace(" ","")
def plus(value):
    value =value .replace(" ","")
    value =value .replace("+-","-")
    value =value  .replace("--","+")
    return value

def mul_dive(value_list):
    aa_list=[]
    for index,element in enumerate(value_list):
        aa=re.findall("[*/]",element)        #寻找
        bb=re.split("[*]",element)          #以* / 分割
        for i,j in enumerate(bb):
            #print(index, element,j)
            print(i,j)
            #print(j)
            #print(aa)
            if i == 1 :
                print('yes')







def backend(value):
    value =re.sub("[()]","",value)
    #value =plus(value )
    print(type(value))


#backend(a)
mul_dive(a)