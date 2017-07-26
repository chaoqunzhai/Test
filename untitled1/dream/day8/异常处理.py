try:
    int('aaaaa')
    li = [11,22]
    li[100]
    c=a+b
except ValueError as a:      #将错误信息封装到a对象里面
    print('aaaa',a)
except KeyError as b:
    print('bbb',b)
except Exception as c:       #如果上面捕捉不到 就到这样。。。。 其中   Exception是所有异常的汇总。
    print('ccc',c)
else:                      #这里是不发生异常 就执行
    print('！！！else')
finally:                   #无论如何 都要执行这段
    print('fianlly!!!')