#__author:  Administrator
#date:  2017/3/26

from django import forms
from bbs import models


class ArticleForm(forms.ModelForm):
    def __new__(cls, *args, **kwargs):
        print("cls",cls)
        for field_name in cls.base_fields:
            field = cls.base_fields[field_name]
            attr_dic = {'class': 'form-control'}
            # if field_name == "body":
            #     attr_dic.update({"id":"article_editor"})
            field.widget.attrs.update(attr_dic)

        return forms.ModelForm.__new__(cls)

    class Meta:
        model = models.Article #attrs
        fields = "__all__"
        exclude = ('priority','author')



