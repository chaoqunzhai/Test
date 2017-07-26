f=open('list','r',encoding='utf-8')
for line in f:
       result=list()
       line=line.strip()
       a=line.split(',')
       #print(a)
       result.append(a)
       #print(type(result))
       #print(type(line))
      # print(result)
       for i,ele in enumerate(result):
             print(i,ele)
      # # a.sort(key=lambda x:x[0][0])
      # print(a)
      # #result.sort(key=lambda x:x[0][0])
      #print(result)
     # result.append(a)
# print(result)
#      for line2 in f1:
#          b = line.split(',')
#          print(b)
#      if len(a) > 0:
#          a[0]=a[1:]
#          #a[0].append(a[0])
#          print(a[0])
#          #b=a[0]
# result=list()
# for line in f.readlines():
#     line=line.strip()
#     result.append(line)
# result.sort()
# print(result)