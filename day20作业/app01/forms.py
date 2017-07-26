from django import forms
import re
from app01 import models


FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)
BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')

def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(str(value)):
        raise forms.ValidationError('手机号码格式错误')



class MailSendForm(forms.Form):
    sender = forms.EmailField()
    receiver = forms.EmailField()
    subject = forms.CharField(max_length=12)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':100,
                                                           'class':'font-color',
                                                           'style':'background-color:lightgreen'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    seat_CHOICES = (('1', 'First',), ('2', 'Second',))
    mobile = forms.IntegerField(validators=[mobile_validate,],
                                error_messages={'required': '手机不能为空'},
                                widget=forms.TextInput(attrs={'class': "form-control",
                                                              'placeholder': '手机号码'})
                                )
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=seat_CHOICES)
    favorite_colors = forms.MultipleChoiceField(
            #required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=FAVORITE_COLORS_CHOICES,
        )

    def clean_sender(self):
        print("validate sender",self.cleaned_data)
        if self.cleaned_data.get("sender") != "alex@126.com":
            self.add_error("sender","Only alex has right to send email!")

        return self.cleaned_data.get("sender")


    def clean(self):
        #所有的clean_field都验证完成后，才会到这里
        print("clean data:::",self.cleaned_data)
        sender = self.cleaned_data.get('sender')
        receiver = self.cleaned_data.get('receiver')

        if sender == receiver:
            raise forms.ValidationError("发送者和接受者不能相同!")
