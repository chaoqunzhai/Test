ain=input('>>')
ain=str(ain)
f=open('haproxy')
while True:
    for i in f.readlines():
    #print(i)
        a=i.strip('\n').strip()
        if ain in list(a):
            print([a].index(ain))
        else:
            print('no')
    #del a[ain]
        #print([a].remove(ain))

