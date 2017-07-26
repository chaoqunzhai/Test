from django import forms
from app01 import models


#如果在form中使用 obj.is_vaild()  就是验证功能
class ArticleFrom(forms.ModelForm):
    #拿不到固定字段的时候，用这个方法
    def __new__(cls, *args, **kwargs):       #重写了new方法，你必须去继承父类的new方法,不然就会导致整个form的失效
        for field_name in cls.base_fields:         #通过cls拿到它的base_fields，base_fields是在里面写死了，通过它可以拿到里面所有的字段
            field = cls.base_fields[field_name]  #   然后拿到所有的字段， 就可以进去判断类型
            attr_dic = {'class':'form-control'}
            # if field_name == "body":
            #     attr_dic.update({"id":"article_editor"})
            field.widget.attrs.update(attr_dic)          #拿到并更新一个样式
        return forms.ModelForm.__new__(cls)

    class Meta:
        model = models.Article
        fields = "__all__"
        exclude=('author','priority')       #隐藏这2个值