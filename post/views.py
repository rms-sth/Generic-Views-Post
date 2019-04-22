from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class PostListView(ListView):
    template_name = 'post/post_list.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = PostForm
        context['com'] = CommentForm
        return context


class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
	    user = self.request.user.id
	    author = User.objects.get(id=user)
	    form.instance.author = author
	    return super().form_valid(form)

 
class CommmentListView(ListView):
	template_name = 'post/post_list.html'
	context_object_name = 'comments'
	model = Comment

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['com'] = CommentForm
	    return context



class CommentCreateView(CreateView):
    template_name = 'post/post_list.html'
    # model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        post_id = self.kwargs['pk']
        post = Post.objects.get(id=post_id)
        form.instance.post = post
        user = self.request.user.id
        author = User.objects.get(id=user)
       	form.instance.author = author
        return super().form_valid(form)

    def get_success_url(self):
    	# post_id = self.kwargs['pk']
    	return reverse('post_list')
	
