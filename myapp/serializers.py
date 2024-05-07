from .models import *
from rest_framework import serializers

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'user', 'content', 'caption', 'likes_count','created_at', 'expiration_date']
        
class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['id', 'user', 'post', 'created_at']
        
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followers
        fields = '__all__'
        
class DirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessage
        fields = '__all__'
        
class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'
        
        