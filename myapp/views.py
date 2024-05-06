from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PostsViewAPI(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        user = self.request.user
        