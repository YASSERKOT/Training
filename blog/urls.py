from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.posts_list, name='posts_list'),
	path('addPost', views.add_post, name='add_post'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit')
]