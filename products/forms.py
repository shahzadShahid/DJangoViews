from django import forms
from django.forms import fields
from django.forms.widgets import Textarea
from .models import Product
from django.shortcuts import render


class ProductForm(forms.ModelForm):
    title      = forms.CharField( widget=forms.TextInput(attrs={'placeholder':' title'}))
    description = forms.CharField(required=False,label='desc', widget=Textarea(attrs={
        'class':'new_class',
        'id':'my_id_for_textarea',
        'rows': 10,
        'columns':1000
    }))
    price       = forms.DecimalField(initial=23.09)
    email      = forms.EmailField()
    class Meta:
        model = Product
        fields = [
            'title','description','price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'ayan' in title:
            raise forms.ValidationError('this is not a valid title')
        return title
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('edu'):
            raise forms.ValidationError('this is not a email')
        return email
            
    

class RawProductForm(forms.Form):
    title      = forms.CharField( widget=forms.TextInput(attrs={'placeholder':' title'}))
    description = forms.CharField(required=False,label='desc', widget=Textarea(attrs={
        'class':'new_class',
        'id':'my_id_for_textarea',
        'rows': 10,
        'columns':1000
    }))
    price       = forms.DecimalField(initial=23.09)