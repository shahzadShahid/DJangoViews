from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Article
from django.views.generic import (
    DetailView, ListView, UpdateView, DeleteView, CreateView

)
from .form import ArticleModelForm
from django.urls import reverse

class ArticleListView(ListView):
    template_name = 'article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    queryset   = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    template_name='article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article,id=id_)

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleCreateView(CreateView):
    template_name = 'article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
 
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    queryset   = Article.objects.all()
    # success_url = '/blog/'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)
    
    def get_success_url(self):
        return reverse('articles:article_list')