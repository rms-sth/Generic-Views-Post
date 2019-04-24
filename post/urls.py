from django.urls import path
from .views import *

app_name = 'post'
urlpatterns = [
	# CLIENT URL PATTERNS
    # CLIENT URL PATTERNS
    # CLIENT URL PATTERNS
    # CLIENT URL PATTERNS
path('', ClientPostListView.as_view(), name='clientpostlist'),
path('create/', ClientPostCreateView.as_view(), name='clientpostcreate'),
path('<int:pk>/comment/', ClientCommentCreateView.as_view(), name='clientcommentcreate'),
path('post/detail/<int:pk>', PostDetailView.as_view(), name='clientpostdetail'),

]