from django import forms
from .models import Post, Comment, PostImage

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('image', 'featured', 'thumbnail', 'active')

class FeedbackForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=200)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    feedback = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)