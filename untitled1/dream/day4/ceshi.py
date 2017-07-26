for i in range(1,10,2):
    print(i)

msg = "又回到最初的起点"
f = open("tofile","w",encoding='utf-8')
print(msg,"记忆中你青涩的脸",sep="|",end="",file=f)

a=[1,3,5,7,8]
b=[5,6,-5,9,10,20,50,70,5,6]
for i in zip(a,b):
    print(i)