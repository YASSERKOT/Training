from django import forms
from .models import Post, Comment, PostImage

from crispy_forms.helper import FormHelper

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

    helper = FormHelper()
    helper.form_show_errors = True

    name = forms.CharField(label="Your name", max_length=10)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    feedback = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        sender = self.cleaned_data['email']
        if not sender.split('@')[1] == "softcatalyst.com":
            msg = "Email is invalid. The email should be a softcatalyst email"
            self.add_error('email', msg)
    """
    def clean_email(self):
        data = self.cleaned_data['email']
        if not data.split('@')[1] == "softcatalyst.com":
            raise forms.ValidationError("Email is invalid. The email should be a softcatalyst email")
        return data
    """