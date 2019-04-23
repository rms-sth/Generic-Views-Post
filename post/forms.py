from django import forms
from .models import Post, Comment

class ClientPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('content', 'author',)

	def clean_client_post(self):
		content = self.cleaned_data.get("content")
    	# emails = User.objects.filter(is_active=True).values_list('email', flat=True)
    	# if email in emails:
    	# 	raise forms.ValidationError("Not a vaid email")
		return content



class ClientCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)