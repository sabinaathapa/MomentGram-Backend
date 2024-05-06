from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here
class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def perform_create(self, serializer):
        serializer.save()
        
class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    
    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        
        username = serializers.validated_data['username']
        password = serializers.validated_data['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            accessToken = str(refresh.access_token)
            
            response_data = {
                "status": "success",
                "data":{
                    "access_token" : accessToken,
                    "refresh_token" : str(refresh)
                },     
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data ={
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Invalid username or password."
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

        