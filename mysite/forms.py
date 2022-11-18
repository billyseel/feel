from . import models
from django import forms


class ContactForm(forms.Form):
    CITY = [
        ['TP', 'Taipei'],
        ['TY', 'Taoyuang'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
        ['KS', 'Kaohsiung'],
        ['NA', 'Others'],
    ]
    user_name = forms.CharField(
        label='your name', max_length=50, initial='chin')
    user_city = forms.ChoiceField(label='citylabel', choices=CITY)
    user_school = forms. BooleanField(label='your school', required=False)
    user_email = forms.EmailField(label='your email')
    user_message = forms.CharField(label='your user', widget=forms.Textarea)


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['mood', 'nickname', 'message', 'del_pass']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = 'Achievement'
        self.fields['nickname'].label = 'Nickname'
        self.fields['message'].label = 'Message'
        self.fields['del_pass'].label = 'delete code'
