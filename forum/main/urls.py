from django.contrib import admin
from django.urls import path
from .views import detail, home, posts, create_post, latest_posts



urlpatterns = [
    path('', home, name='home'),
    path('detail/<slug>/', detail, name='detail'),
    path('posts/<slug>/', posts, name='post'),
    path('create_post/', create_post, name='create_post'),
    path('latest_posts/', latest_posts, name='latest_posts')
]