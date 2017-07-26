#_*_coding:utf-8_*_
#时间2016:11:5   1:13
'''

'''
#
def show():
    f = open('list', 'r', encoding='utf-8')
    coun = 0
    for line in f.readlines():
        coun += 1
        line=line.strip()
        a = line.split(',')
        bnew = str(coun) + str(a)
        #a.sort(key=lambda x: x[0][0])
        print(bnew)
    f.close()
def add(date):
    backend=fetch(date)
    new_list=[]
    if not backend:
        print('\033[32m提示:不在列表中，可以增加\033[0m')  # 插入语句 insert name age iphone dept,
        with open('list','r',encoding='utf-8') as read_file,\
            open('list_add','w',encoding='utf-8') as write_file:
            if date[0][:6] == 'insert':     # 用简易语法如：insert 翟超群 （后面名字输入不存在才可）   即可进去下一步进行增加，比较二逼的写法。
                print('\033[31m如进去add环节，直接输入要增加内容即可\033[0m')
                new_date = input('ADD>>').split(',')
                #new_list.append(date[0][7:])
                new_list.append(new_date[0])
                print(new_date[0])
            else:
                print('\033[35m输入正确语句,\
                        提示语法:insert name age iphone dept \033[0m')
            for r_line in read_file:
                write_file.write(r_line)
            for new in new_list:
                #print(type(new))
                write_file.write('\n'+ new + '\n')
    else:
        print('\033[32m在列表中，不可以重复增加\033[0m')
def remove(date):
    rebackend=fetch(date)
    if not rebackend:
        if date[:6] == 'select':           # 请先输入 select name 查询才可以进入下一个del环境  就可以进行下去
            print('\033[34m 无此条信息，无法删除\033[0m')
            return
    else:
        print('\033[31m在列表中可以删除\033[0m')
        re_date=input('DEL>>').strip()           # 在del模式下 请输入 del name 或者del ID 即可删除！！
        if re_date[:3] == 'del':
            #print('yes')
            with open('list', 'r', encoding='utf-8') as re_old, \
                    open('list_re', 'w', encoding='utf-8') as re_new:
                for a in re_old:
                    cx = a.strip().split(',')
                    try:
                        if cx[0] == date[0][7:]:
                            print(cx)     #
                            a=a.replace(cx,0)
                        re_new.write(a)
                    except TypeError:
                        print('\033[33m替换成功!!!!\033[0m')
def change(date):
    rebackend = fetch(date)
    new = ''
    if not rebackend:
        if date[:6] == 'select':
            print('\033[34m 无此条信息，无法更改\033[0m')
            return
    else:
        print('\033[31m在列表中可以更改\033[0m')
        re_date = input('UPDATE>>').split(',')
        #if re_date[:6] == 'update':
        with open('list', 'r', encoding='utf-8') as re_old, \
                open('list_update', 'w', encoding='utf-8') as re_new:
            for a in re_old:
                cx = a.strip().split(',')
                try:
                    if cx[0] == date[0][7:]:
                        #print(cx)
                        #new=new + re_date
                        print(new)
                        a=a.replace(cx,new)
                    re_new.write(a)
                except TypeError:
                    print('\033[33m替换成功!!!!\033[0m')
def fetch(date):
    result = []
    agelist=[]
    with open('list','r',encoding='utf-8') as f1:
        coun = 0
        for a in f1:
            coun += 1
            cx=a.strip().split(',')
            anew = str(coun) + str(cx)            #使用超级模糊查询  select 翟超群  或者 select age>20 或者select dept=IT  这样简易查询
            if date[0][:6] == 'select'or date[0][:6] =='insert'or date[0][-7:-3] == 'age':
                if cx[0] == date[0][7:]:
                    result.append(anew)
                if date[0][-3:-2] == '>' or date[0][:7] == 'select' and date[0][-7:-3] == 'age':
                    if cx[1] > date[0][-2:]:
                        agelist.append(anew)
                        print(anew)
                if date[0][-2:] in cx[3] and date[0][-7:-3] == 'dept':
                    result.append(anew)
                    print(anew)
                    #print(cx.count(cx[0]))
            else:
                #print('\033[35m语法使用错误,使用<<select name>> or <<select age>22>> 二逼小语法\033[0m')
                break
        for a in result:
            print(a)
        return result
def bay(date):
    pass
if __name__ == '__main__':
    print('\033[32m支持语法 select name\033[0m')
    print('\033[32m支持语法 select dept = "IT"\033[0m')
    print('\033[32m支持语法  select age>22\033[0m')
    function='''
    1:增
    2:删
    3:改
    4:查
    5:ALL
    6:退
    '''
    function_dict={
        '1':add,
        '2':remove,
        '3':change,
        '4':fetch,
        '5':show,
        '6':bay
    }
    while True:
         print(function)
         choice=input('function>>: ').strip()
         if len(choice) == 0 or choice not in function_dict:continue
         if choice == '6':break
         if choice == '5':
             show()
             continue
         date=input('Sql>>>').split(',')
         if date == 'q':break


         function_dict[choice](date)



         #name,age,phone,dept,enroll_date
         #select zhaichaoqun,it,1312378203