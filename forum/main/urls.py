from django.contrib import admin
from django.urls import path
from .views import detail, home, posts

urlpatterns = [
    path('', home, name='home'),
    path('detail/', detail, name='detail'),
    path('posts/', posts, name='post'),
]