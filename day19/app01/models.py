from django.db import models

# Create your models here.


#类代表表，字段代表列
#类的对象 --->代指数据的行
class UserInfo(models.Model):      #表
    uid = models.AutoField(primary_key=True)        #列   并且是主键,是自增的
    hostname = models.CharField(max_length=64)  #列
    passwd = models.CharField(max_length=64)    #列
    port = models.IntegerField()    #列
