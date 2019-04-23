from django import forms
from .models import Post, Comment

class ClientPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('content', )



class ClientCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)