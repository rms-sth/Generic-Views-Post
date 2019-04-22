from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	content = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	

	class Meta:
		ordering = ('-created_date',)

	def __str__(self):
		return f'Post by : {self.author} on {self.created_date} => [{self.content[:20]}]'

	# def get_absolute_url(self):
	# 	return reverse("post_detail", kwargs = {"pk": self.pk})


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments', on_delete = models.CASCADE)
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	body = models.TextField()
	created_date = models.DateTimeField(auto_now_add = True)
	updated_date = models.DateTimeField(auto_now_add = True)

	class Meta:
		ordering = ('-created_date',)

	def __str__(self):
		return f'Comment by {self.author} on {self.post}'
