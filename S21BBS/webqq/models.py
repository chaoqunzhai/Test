from django.db import models
from app01.models import UserProifle
# Create your models here.

class QQgroup(models.Model):
    name = models.CharField(max_length=64)
    bref = models.CharField(max_length=128,blank=True,null=True)
    notification = models.CharField(max_length=128,verbose_name="群公告",blank=True,null=True)

    members= models.ManyToManyField(UserProifle)

    max_members = models.PositiveSmallIntegerField(default=200)       #正整数字段

    def __str__(self):

        return self.name
