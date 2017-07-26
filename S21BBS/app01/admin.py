from django.contrib import admin

# Register your models here.
from app01 import models
# Register your models here.

#自定制django admin, 然后你下面admin.site.register 里面也要加入这个自定义的类
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','p_node','user','date','comment')

admin.site.register(models.Article)
admin.site.register(models.UserProifle)
admin.site.register(models.Tag)

admin.site.register(models.Comment,CommentAdmin)

admin.site.register(models.Like)
admin.site.register(models.PrivateMail)
admin.site.register(models.Category)