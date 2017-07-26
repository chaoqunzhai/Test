with open('list','r',encoding='utf-8') as f1:
    for line in f1:
        b=0
        #print(type(line.strip()))
        #print(line.strip().split(','))
        put=line.strip().split(',')
        print(put)