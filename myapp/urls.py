from django.urls import path
from .views import *


urlpatterns = [
    path('posts/', PostsViewAPI.as_view(), name='posts'),
    path('likes/<post_id>/', LikesViewAPI.as_view(), name='likes'),
    path('comments/<post_id>/', CommentViewAPI.as_view(), name='comments'),
    path('followers/<username>/',FollowersViewAPI.as_view(), name='followers'),
    
]
