from django.urls import path
from .views import *


urlpatterns = [

path('', PostListView.as_view(), name='post_list'),
path('create/', PostCreateView.as_view(), name='post_create'),
# path('view/', CommmentListView.as_view(), name='view_comment'),
path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),

]