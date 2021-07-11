# from blog.views import article_create, article_detail, article_list
from django.urls import path
from .views import (
    ArticleDetailView,
    ArticleListView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
    
)
app_name = 'articles'
urlpatterns=[
    path('',ArticleListView.as_view(),name='article_list'),
    path('<int:id>/detail',ArticleDetailView.as_view(),name='article_detail'),
    path('create/',ArticleCreateView.as_view(),name='article_create'),
    path('<int:id>/update/',ArticleUpdateView.as_view(),name='article_update'),
    path('<int:id>/delete/',ArticleDeleteView.as_view(),name='article_delete'),
]
