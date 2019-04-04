from django.contrib import admin
from django.urls import path, include
from . import views

from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

urlpatterns = [
	#path('', views.posts_list, name='post_list'),
	path('', views.PostListView.as_view(), name='post_list'),
	#path('addPost', views.add_post, name='add_post'),
	path('post/add/', login_required(TemplateView.as_view(template_name="blog/addPost.html")), name='add_post'),
	#path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
	#path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('post/<int:pk>/edit/', login_required(TemplateView.as_view(template_name="blog/addPost.html")), name='post_edit'),
	#path('post/<int:pk>/remove', views.post_remove, name='post_remove'),
	path('post/<int:pk>/remove', login_required(TemplateView.as_view(template_name="blog/addPost.html")), name='post_remove'),
	path('drafts/', views.post_draft_list, name='post_draft_list'),
	path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
	path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
	path('post/<int:pk>/image/', views.add_image_to_post, name="add_image_to_post"),
	path('comment/<int:pk>/remove/', views.remove_comment, name="remove_comment"),
	path('comment/<int:pk>/approve/', views.approve_comment, name="approve_comment"),
	path('comment/<int:pk>/desapprove/', views.desapprove_comment, name="desapprove_comment"),
	
	path('api/posts/', views.ListPostView.as_view(), name="api_post_list"),
	path('api/post/<int:pk>/', views.SinglePostView.as_view(), name="api_post_detail"),
	
	path('contact/', views.send_feedback, name="send_feedback_email"),
	path('contact/sent/', views.feedback_email_sent, name="thanks_page")
]