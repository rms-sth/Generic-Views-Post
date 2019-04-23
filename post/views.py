from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import ClientPostForm, ClientCommentForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import JsonResponse
from .mixins import AjaxableResponseMixin


class ClientPostListView(ListView):
    template_name = 'clienttemplates/post/clientpostlist.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = ClientPostForm
        context['com'] = ClientCommentForm
        return context


# Non-Ajax Posting
# class ClientPostCreateView(CreateView):
#     template_name = 'clienttemplates/post/clientpostlist.html'
#     form_class = ClientPostForm
#     # model = Post
#     success_url = reverse_lazy('clientpostlist')

#     def form_valid(self, form):
#       user = self.request.user.id
#       author = User.objects.get(id=user)
#       form.instance.author = author
#       return super().form_valid(form)


class ClientCommmentListView(ListView):
    template_name = 'clienttemplates/post/clientpostlist.html'
    context_object_name = 'comments'
    model = Comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['com'] = ClientCommentForm
        return context


class ClientCommentCreateView(CreateView):
    template_name = 'clienttemplates/post/clientpostlist.html'
    # model = Comment
    form_class = ClientCommentForm

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
        return reverse('post:clientpostlist')


#Ajax Posting
class ClientPostCreateView(AjaxableResponseMixin, CreateView):
    template_name = 'clienttemplates/post/clientpostlist.html'
    form_class = ClientPostForm
    success_url = 'clientpostlist'


