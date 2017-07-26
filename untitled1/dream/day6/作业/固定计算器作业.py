import re
def plus(value):
    value =value .replace(" ","")
    value =value .replace("+-","-")
    value =value  .replace("--","+")
    return value
def konge(value):
    value=value.replace(" ","")
    back=re.compile("\([^()]*\)")
    c=back.findall(value)
    print(c)
    value_1 = re.sub("[()]","",c[0])
    value_2 = re.sub("[()]","",c[1])
    value_3 = re.sub("[()]","",c[2])
    value_4 = re.sub("[()]","",c[3])
    print('\033[36m;切分处理括号 %s %s %s %s \033[0m'%(value_1, value_2, value_3,value_4))
    for i,j in enumerate(value_1):
        if j == '/':
            value_1=int(value_1[:i]) / int(value_1[i+1:])
            print('\33[34;1m计算(-40/5)的值为:%s\33[0m' % (value_1))
    value_2=re.split("\+",value_2)
    print('\33[34;1m将要拆分的列表为:%s\33[0m' %(value_2))
    value_2_1=value_2[0]
    value_2_2=value_2[1]
    value_2_3=value_2[2]
    for e,q in enumerate(value_2_1):
        if q == '-':
            e_1=e
            value_2_1_1=value_2_1[e_1-1]
        elif q == "*":
            e_2=e
            value_2_1_2=value_2_1[e_2 - e_1]
        elif q == "/":
            e_3 = e
            value_2_1_3 = value_2_1[e_3 + 1]
            value_2_1_4 = value_2_1[e_3 - 1]
            value_2_1_a= float(value_2_1_2) * float(value_2_1_4)
            value_2_1_b=int(value_2_1_a) / int(value_2_1_3)
            if value_2_1_b:
                value_2_1_c=float(value_2_1_1) - float(value_2_1_b)
                value_2_1=value_2_1_c
                print('\33[34;1m计算(9-2*5/3)的值为:%s\33[0m'%(value_2_1))
    for w,z in enumerate(value_2_2):
        if z == '/':
            w_1=w
            value_2_2_1=value_2_2[w_1-1]
            value_2_2_2 = value_2_2[w_1 + 1]
            value_2_2_a=float(value_2_2_1) / float(value_2_2_2)
            if '*' in value_2_2[w_1:]:
                value_2_2_3=value_2_2.index('*')
                value_2_2_4=value_2_2_3*2
                value_2_2_5= value_2_2[value_2_2_3 +1 :value_2_2_4]
                value_2_2_c=float(value_2_2_a) * float(value_2_2_5)
                value_2_2_d=float(value_2_2_c) / float(value_2_2[7])
                value_2_2_e=float(value_2_2_d) * float(value_2_2[9:])
                print('\33[34;1m计算（7/3*99/4*2998）的值为:%s\33[0m ' %(value_2_2_e))
            break
    for a,b in enumerate(value_2_3):
        if b == '*':
            a_1=a
            value_2_3_1=value_2_3[:a_1]
        elif b == '/':
            a_2=a
            value_2_3_2=value_2_3[a_2 +1:]
            value_2_3_a=value_2_3[a_1+1:a_2]
            value_2_3_c=float(value_2_3_1) * float(value_2_3_a)
            value_2_3_d=float(value_2_3_c) / float(value_2_3_2)
            print('\33[34;1m计算(10*568/14)的值为:%s\33[0m'%(value_2_3_d))
            if float(value_2_3_d) > 0:
                all_1=float(value_2_1) + float(value_2_2_e) + float(value_2_3_d)
                all_2=value_1 * all_1 +30
                #global all_2
                print('\33[34;1m(9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )值为%s\33[0m' %(all_1))
                print('\33[34;1m(60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 ))值为%s\33[0m' %(all_2)  )
    for g,f in enumerate(value_3):
        if f == "*":
            f_1=g
            value_3_1=value_3[f_1+1:]
            value_3_2=value_3[:f_1]
            value_3_a=float(value_3_1) * float(value_3_2)
    for h,h_1 in enumerate(value_4):
        if h_1 == "-":
            h_1=h
            value_4_3=value_4[:h_1]
        elif h_1 == "*":
            h_1=h
            value_4_1=value_4[h_1 +1:]
            value_4_2=value_4[3:h_1]
            value_4_a=float(value_4_1) * float(value_4_2)
            value_4_b=float(value_4_3) - float(value_4_a)
            if float(value_4_b):
                all_3=float(value_3_a) / float(value_4_b)
                all_4=float(all_2) + float(-all_3)
                print('\33[34;1m(60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2)值为%s\33[0m' %(all_4))
    for i_1, j_1 in enumerate(value):
        if j_1 == "(":
            j_1 = i_1
            j_2=value[:j_1]
            if "*" in j_2:
                ovear=float(j_2[:1]) - float(j_2[2:3]) * float(all_4)
                print('\33[34;1m1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )  %s\33[0m' %(ovear))
            break


if __name__=='__main__':
    a='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    konge(a)
