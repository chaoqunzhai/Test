from django import template
from django.utils.safestring import mark_safe
register = template.Library()

#register是必须这样写！
@register.filter
def site(value,num):
    print(value)
    return 'zhaichaoqun' + '---->' +value +  str(num)
@register.filter
def site_two(value,num):
    temp = "<a href=http://cnblogs.com?t=%s>%s</a>" %(num,value)       #这样的话可以省去编写复杂的html，把前端的值传入到这里，
    return mark_safe(temp)


@register.simple_tag
def site_three(v1,v2,v3):
    return v1+v2+v3