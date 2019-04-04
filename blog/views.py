from django.utils import timezone
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostForm, CommentForm, ImageUploadForm, FeedbackForm

from django.views import generic
from django.urls import reverse

"""
def posts_list(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/mainPage.html', {'posts' : posts})
"""

class PostListView(generic.ListView):
	template_name = 'blog/mainPage.html'
	context_object_name = 'posts'
	def get_queryset(self):
		"""Return the lastest post published on the blog by the admin."""
		return Post.objects.filter(created_date__lte=timezone.now()).order_by('published_date')

"""
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/showPost.html', {'post':post})
"""

class PostDetailView(generic.DetailView):
	template_name = 'blog/showPost.html'
	model = Post
	context_object_name = 'post'

"""
@login_required
def add_post(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid() :
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/addPost.html', {'form': form})
"""

class PostCreateView(generic.edit.CreateView):
	template_name = 'blog/addPost.html'
	model = Post
	form_class = PostForm
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(PostCreateView, self).form_valid(form)

"""
@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/addPost.html', {'form': form})
"""

class PostUpdateView(generic.edit.UpdateView):
	template_name = 'blog/addPost.html'
	model = Post
	form_class = PostForm


"""
@login_required
def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('post_list')
"""
class PostDestroyView(generic.edit.DeleteView):
#	template_name = 'blog/post_confirm_delete.html'
	model = Post

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('post_detail', pk=pk)


@login_required
def add_comment_to_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def approve_comment(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.approve()
	return redirect('post_detail', pk=comment.post.pk)


@login_required
def desapprove_comment(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.desapprove()
	return redirect('post_detail', pk=comment.post.pk)

@login_required
def remove_comment(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.delete()
	return redirect('post_detail', pk=comment.post.pk)


@login_required
def add_image_to_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			image = form.save(commit=False)
			image.post = post
			image.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = ImageUploadForm()
	return render(request, 'blog/add_image_to_post.html', {'form': form})


from django.core.mail import send_mail

def send_feedback(request):
	if request.method == "POST":
		form = FeedbackForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			feedback = form.cleaned_data['feedback']
			cc_myself = form.cleaned_data['cc_myself']

			recepients = ['yasserkotrsi@softcatalyst.com']
			if cc_myself:
				recepients.append(email)
			send_mail(subject, feedback, email, recepients, fail_silently=False)	
			return redirect('thanks_page')
	else:
		form = FeedbackForm()
	return render(request, 'contact/send_feedback_email.html', {'form':form}) 

def feedback_email_sent(request):
	return render(request, 'contact/feedback_email_sent.html')


from rest_framework import status
from .serializers import PostSerializer
from rest_framework.views import APIView

#### REST FRAMEWORK API VIEWS:
class ListPostView(APIView):
	def get(self, request):
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)
	def put(self, request):
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, 
		status=status.HTTP_400_BAD_REQUEST)

class SinglePostView(APIView):
	def get(self, request, pk):
		post = get_object_or_404(Post, pk=pk)
		serializer = PostSerializer(post)
		return Response(serializer.data)

	def delete(self, request, pk):
		post = get_object_or_404(Post, pk=pk)
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)		