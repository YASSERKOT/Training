from django.db import models
from django.conf import settings
from django.utils import timezone

from django.urls import reverse

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.CharField(max_length=5000)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)
	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
	post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
	author = models.CharField(max_length=200)
	text = models.CharField(max_length=5000)
	created_date = models.DateField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def desapprove(self):
		self.approved_comment = False
		self.save()
	
	def __str__(self):
		return self.text

	def get_absolute_url(self):
		return reverse('comment')

class PostImage(models.Model):
	post = models.ForeignKey('blog.Post', on_delete=models.DO_NOTHING)
	image = models.ImageField(upload_to='blog/images/')
	featured = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)
	thumbnail = models.BooleanField(default=False)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.post.title
	def get_absolute_url(self):
		return reverse('postimage')