from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.home, name='blog'),
    path('poemlist/', views.poemlist, name='poemlist'),
    path('poem_detail/<int:pk>/', views.poem_detail, name='poem_detail'),
    path('bloglist/', views.bloglist, name='bloglist'),
    path('blog_detail/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('about/', views.about, name='about'),
]
