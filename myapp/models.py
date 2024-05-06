from django.db import models
import uuid
from accounts.models import CustomUser
# Create your models here.
class Posts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    caption = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.caption
    
class Likes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class Comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class Followers(models.Model):
    id = models.AutoField(primary_key=True)
    follower_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='follower')
    following_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='following')
    
    def __str__(self):
        return self.follower_id.username + " is following " + self.following_id.username
    
class DirectMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return self.sender.username + "send a message to" + self.receiver.username

class Notifications(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username + " has " + self.type + " from " + self.source
    
 
    
    