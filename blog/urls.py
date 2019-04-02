from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.posts_list, name='post_list'),
	path('addPost', views.add_post, name='add_post'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('drafts/', views.post_draft_list, name='post_draft_list'),
	path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
	path('post/<int:pk>/remove', views.post_remove, name='post_remove'),
	path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
	path('comment/<int:pk>/remove/', views.remove_comment, name="remove_comment"),
	path('comment/<int:pk>/approve/', views.approve_comment, name="approve_comment"),
	path('comment/<int:pk>/desapprove/', views.desapprove_comment, name="desapprove_comment")

]