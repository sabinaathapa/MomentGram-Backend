from django.urls import path
from .views import *


urlpatterns = [
    path('posts/', PostsViewAPI.as_view(), name='posts'),
    
]
