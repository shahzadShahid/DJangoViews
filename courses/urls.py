from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CourseView,  CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView
app_name ='courses'
urlpatterns =[
    path('',CourseView.as_view(template='home.html'),name='course-view'),
    path('<int:id>/',CourseView.as_view(), name='course-detail'),
    path('list/',CourseListView.as_view(), name='course-list'),
    path('create/', CourseCreateView.as_view(), name ='course-create'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name ='course-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name ='course-delete')
]