from  django.template import Library
from django.utils.safestring import mark_safe

register = Library()

@register.simple_tag
def truncate_upload_img(img_src):
    print(dir(img_src))
    print(img_src.name)
    return img_src.name.lstrip("/uploads/")


@register.simple_tag
def render_paginator_btn(articles,page):

    current_page = articles.number
    if abs(current_page - page) <= 5 :#display button
        ele = """<li ><a href="?page={page}">{page}</a></li>""".format(page=page)
        return mark_safe(ele)

    return ''