from django.urls import path
from .views import *

urlpatterns = [
    path('user_register/', UserRegisterView.as_view(), name='user_register'),
    path('user_login/', UserLoginView.as_view(), name='user_login'),
    
]
