##
##在PyCharm中编写，在此环境下运行更佳
print('\033[34m----自动化修改配置文件----\033[0m')
#ainput={'1':'增加','2':'删除','3':'修改','4':'查询'}
alist=[['1:增加'],['2:删除'],['3:修改'],['4:查询'],['5:退出']]
#f=open('haproxy')
b='\t'
while True:
    f = open('haproxy')
    for i in alist:
        print(i[0],end='')
    print()
    ainput=input('\033[32m请输入要进行的操作>>:\033[0m')
    if ainput.isdigit():
        ainput=int(ainput)
        if ainput == 1:
            binput = input('请输入要添加的backend的模块名称>>:')
            for i in f.readlines():
                a=i.strip('\n').strip()
                if binput in a and len(binput) >= 2:
                    print('\033[35m------模块存在------\033[0m')
                    f1 = open('haproxy', 'a+')
                    cinput = input('请输入IP>>:')
                    dinput = input('请输入weight>>：')
                    einput = input('请输入maxconn>>:')
                    f1.write('\n' + 'backend' + ' ' + binput)
                    f1.write('\n' + b + b + 'server' + ' ' + cinput + ' ' + 'weight' + ' ' + dinput + ' ' + 'maxconn' + ' ' + einput)
                    f1.close()
                    print('\033[35m新加入值为 [backent:%s][IP:%s][weight:%s][maxconn:%s]\033[0m' % (
                    binput, cinput, dinput, einput))
                    break
                if ainput == 'b' or binput == 'b':
                    exit()
        if ainput == 2:
            delput = input('请输入要删除的模块名称>>')
            f2=open('haproxy-del','w')
            for line in f:
                if delput in line:
                    line= ' '
                f2.write(line)
                print('\033[35m已经删除\033[0m')
            f.close()
            f2.close()
            continue
        if ainput == 3:
             oldfile = input('请输入要修改的模块名称>>:')
             newfile = input('请输入新名称>>:')
             f3=open('haproxy-new','w')
             for e in f:
                 if oldfile in e:
                     e=e.replace(oldfile,newfile)
                     print('\033[35m修改成功\033[0m')
                 f3.write(e)
             f3.flush()
             f3.close()
        if ainput == 4:
            hop = input('请输入要查看的模块名称>>:')
    if ainput == 5 or ainput == 'q' or ainput == 'Q':
        print('已退出')
        break
    else:
        print('\033[36m------请重新输入或者按Q退出------\033[0m')

    f.close()