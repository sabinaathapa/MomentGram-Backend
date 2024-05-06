from django.shortcuts import render
from .serializers import *
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
class PostsViewAPI(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    # permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        user = self.request.user
        #Create serializer with data , including the user
        serializer = self.get_serializer(data=request.data, context = {'user': user})
        serializer.is_valid(raise_exception=True)
        #Call perform create to save the data to the database
        self.perform_create(serializer)
        #Return success response
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        