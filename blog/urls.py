from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
  path('',views.home,name='blog-home'),
  path('profile/<str:pk>',views.userProfile,name='blog-user-profile'),
  path('post/<str:pk>',views.createBlog,name='blog-create'),
    
]