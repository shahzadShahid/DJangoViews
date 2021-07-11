from typing import ContextManager
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Course
from .forms import CourseModelForm
#BASE VIEW Class = View

class CourseDeleteView(View):
    template_name = 'course_delete.html'
    def get_object(self):
        id = self.kwargs.get('id')
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')



class CourseUpdateView(View):
    template_name = 'course_update.html'
    def get_object(self):
        id = self.kwargs.get('id')
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                form = CourseModelForm()
            context['object'] = obj
            context['form'] = form
            return render(request, self.template_name, context)




class CourseCreateView(View):
    template_name = 'course_create.html'
    def get(self, request, *args, **kwargs):
        form = CourseModelForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    




class CourseListView(View):
    template_name = 'course_list.html'
    queryset = Course.objects.all()

    def get(self, request, *args, **kwargs):
        context = {
            'object_list': self.queryset
        }
        return render(request, self.template_name, context)



class CourseView(View):
    template = 'course_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request,self.template,context)
