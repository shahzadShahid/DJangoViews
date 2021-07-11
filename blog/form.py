from courses.models import Course
from typing import Text
from django import forms
from django.forms import fields
from .models import Article
from django.forms.widgets import Textarea



class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title','content','active'
        ]

# class RawArticleForm(forms.Form):
#     title  = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'your_title'}))
#     about  = forms.CharField(required=True,label='info',widget=Textarea(attrs={
#         'id':'my_id12',
#         'rows': 10
#     }))
#     endnote = forms.CharField(required=False,label='conclusion',widget=forms.TextInput(attrs={'placeholder':'moral'
#     }))