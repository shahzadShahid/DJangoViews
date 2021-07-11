from django.shortcuts import redirect, render
from django.http import HttpResponse


def home_view(request,*args, **kwarg):
   return render(request, 'home.html', {})


def about(request,*args, **kwargs):
    my_context = {
        'my_text':'this is for us',
        'my_number':1233,
        'my_list':[22,434,'dk','ABC'],
        'my_html': '<h1>Hello world</h1>'
    }
    return render(request, 'about.html', my_context)
