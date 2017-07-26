def tal(self,msg):
    print("%s is talking:%s" %(self.name,msg))

def __init__(self,name):
    self.name = name

Aa = type("Dog",(object,),{"ceshi":tal,'__init__':__init__})

d=Aa('金毛')
d.ceshi('温顺')