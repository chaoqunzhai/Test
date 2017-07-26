#-*- coding:UTF-8 -*-
import  os
shop=[]
shoplist=[
    ["iphone",5800],
    ["mac",15800],
    ["office",30],
    ["apple",5],
    ["vip服务",0]
]
print('\033[45m**********(本系统在windows环境下执行)*********\033[0m')
print('\033[35m**********欢迎来到永辉超市*********\033[0m')
print('\033[35m**********本店可实现充值，办理VIP*********\033[0m')
print('\033[31m提醒:请输入您的工资。如若退出本超市请按Q\033[0m')
gonzi = input("薪水>>:")
if gonzi.isdigit():
    gonzi=int(gonzi)
    old = input('\033[35m **您是否来过本商城（YES/NO>>:\033[0m')
    if old == 'yes' or old == 'YES':
        alist = 'C:\shop.txt'
        if os.path.exists(alist):
            oldput = open(alist, 'r')
            print('\033[32m********您的购物车是********\033[0m')
            print(oldput.read())
            print('\033[35m********end*************\033[0m')
        else:
            print('again,go shoplist!!!  （核对系统，您没有来过此店）')
    else:
        pass
    while True:
        for i,ele in enumerate(shoplist):
            print(i,ele[0],ele[1])
        #break
        auser = input('请选择商品编号>>:')
        if auser.isdigit():
            auser=int(auser)
            if auser < len(shoplist) and auser >= 0:    #输入的编号 不能大于商品的列表个数
                buser=shoplist[auser]               #根据用户输入的编号，来判断寻到到列表的下标数
                if buser[1] <= gonzi:               # 根据上层的下标数，采用列表中带列表的方式，寻到价格
                    shop.append(buser)
                    gonzi -= buser[1]
                    print('您购买了\033[31m%s\033[0m,您的余额还有 \033[41m%s\033[0m ' %(buser,gonzi))
                else:
                    pass
                    while True:
                        money = input('是否充值(yes/no)>>:' )
                        if money == 'yes' or money == 'YES':
                            amoney=input('充钱栏**:')
                            amoney = int(amoney)
                            gonzi=amoney+gonzi
                            #print(newmoney)
                            break
                        else:
                            print('多赚钱吧')
                            break
            else:
                print('\033[42m超出编号!\033[0m')
            if auser == 4 :
               # newshop=[]
                avip=input('请填写会员(cq)>>：')
                if avip == "cq":
                    cvip = input('请填写新增商品(英文)>>：')
                    for g in range(30):
                        dvip=input('您期望的价格>>>:')
                        if dvip.isdigit():
                            dvip=int(dvip)
                            newshop=shoplist.copy()
                            #newshop[4].append([cvip])
                            newshop.insert(5,[cvip,dvip])
                            print(newshop)
                            break
                elif avip == 'Q' or auser == 'q':
                    print('退出会员模式')
                else:
                    print('\033[31myou do is VIP!\033[0m')
                    continue
        elif auser == 'Q' or auser == 'q':
            print(shop)
            #print(newshop)
            #myshop=set(shop)
            #for item in myshop:
             #   print(item,shop.count(item))
            if len(shop) > 0:
                fo = open("c:\shop.txt",'a+')
                pre=str(shop)
                fo.write(pre)
                fo.flush()
                fo.close()
            print('\033[31m您的清单已经录入系统，欢迎下次光临\033[0m')
            print('\033[45m会员须知如没有您需要的商品，请填写商品，(再次来本店按4)本店会尽快增货\033[0m')
            exit()
        else:
            print('\033[5m\033[31m请输入编号，不要捣乱\033[0m\033[0m')

else:
    exit('( ^_^ )/~~拜拜,  穷..')