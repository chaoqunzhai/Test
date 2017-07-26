from  django.template import Library
from django.utils.safestring import mark_safe

register = Library()

@register.simple_tag
def truncate_upload_img(img_src):
    print(img_src.name,img_src.name.lstrip('/uploads/'))
    # return img_src.name.lstrip('/uploads/')
    return img_src.name.split('/')[1]



@register.simple_tag
def redner_paginator_btn(articles,page):

    current_page = articles.number          #前端写的自定义模板传入了articles的值，这个值是在views中生成的django分页方法，所以这里还可以使用这个articles.number方法
    if abs(current_page - page) <= 3:
        htmle = """<li><a href="?page={page}">{page}</a></li>""".format(page=page)
        return mark_safe(htmle)               #把写的html返回给前端中的自定义模块区域，
                                        #对于不小于3的就会返回个none
    return ''