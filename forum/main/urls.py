from django.contrib import admin
from django.urls import path
from .views import detail, home, posts

urlpatterns = [
    path('', home, name='home'),
    path('detail/<slug>/', detail, name='detail'),
    path('posts/<slug>/', posts, name='post'),
]