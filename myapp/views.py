from django.shortcuts import render
from .serializers import *
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from django.shortcuts import get_object_or_404


# Create your views here.

#Post View
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
        

#Like View
class LikesViewAPI(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        user = self.request.user
        
        #Getting the post to like
        post_id = self.kwargs.get('post_id') #post id is passed from the url
        try:
            post = Posts.objects.get(id=post_id)
        except Posts.DoesNotExist:
            return Response({'error': 'Post does not exist'}, status=status.HTTP_404_NOT)
        
        #Checking if the user has alreday liked the post
        existing_like = Likes.objects.filter(user=user, post=post).first()
        if existing_like:
            #Unlike
            existing_like.delete()
            post.likes_count -= 1
            post.save()
            return Response({'message':'Post Unliked'}, status=status.HTTP_200_OK)
        else:
            #Like
            serializer = self.get_serializer(data={'post':post.id, 'user':user.id}, context={'user': user})
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            post.likes_count += 1
            post.save()
            return Response({'message':'Post Liked'}, status=status.HTTP_201_CREATED)
        
#Comment View
class CommentViewAPI(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        user = self.request.user
        
        #Getting post to comment
        post_id = self.kwargs.get('post_id')
        try:
            post = Posts.objects.get(id=post_id)
        except Posts.DoesNotExist:
            return Response({'error': 'Post does not exist'}, status=status.HTTP_404_NOT)
        
        serializer = self.get_serializer(data= request.data, context = {'user': user, 'post':post})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#Followers View
class FollowersViewAPI(generics.CreateAPIView):
    queryset = Followers.objects.all()
    serializer_class = FollowersSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        user_to_follow = get_object_or_404(CustomUser, username=self.kwargs.get('username'))
        existing_follow = Followers.objects.filter(follower_id=user, following_id=user_to_follow).first()
        if existing_follow:
            existing_follow.delete()  # Unfollow
            user_to_follow.followers_count -= 1
            user.following_count -= 1
            user_to_follow.save()
            user.save()
            return Response({'message': 'User Unfollowed'}, status=status.HTTP_200_OK)
        else:
            serializer.save(follower_id=user, following_id=user_to_follow)
            user_to_follow.followers_count += 1
            user.following_count += 1
            user_to_follow.save()
            user.save()
            return Response({'message': 'User Followed'}, status=status.HTTP_201_CREATED)
     

        
    
    
        
        
        
            
            
        
        