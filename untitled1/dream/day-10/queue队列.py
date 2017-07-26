import queue

###先进先出
q1=queue.Queue(maxsize=3)          #这里设置是可以存放多少个队列  如果设置了3个 但是q.put达到3个以上  ，就会阻塞  因为这是队列 先进先出
q1.put(1)
q1.put(2)
q1.put(3)
q1.empty()
###权重
q2=queue.PriorityQueue()
q2.put([6,'alex'])
q2.put([3,'zhaichaoqun'])
q2.put([10,'renchenghon'])

###后进先出
q3=queue.LifoQueue()
q3.put([6,'alex'])
q3.put([3,'zhaichaoqun'])
q3.put([10,'renchenghon'])


print(q1.empty()) #判断是不是为空   不空为False
print(q1.full())    #判断是不是满
print(q1.qsize())  #队列大小

#因为是队列  不能跳着取。 必须一个一个取 遵循先进先出
print(q1.get())  #get是用来取第一个值   并在队列中取消这个
print(q1.get())  #get是用来取第二个值
print(q1.get())  #get是用来取第三个值
print('取完后队列',q1.qsize())

print(q2.get())
print(q2.get())
print(q2.get())

print('---')
print(q3.get())
print(q3.get())
print(q3.get())