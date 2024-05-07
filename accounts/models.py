from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


#User Model
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='profile_pictures')
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
    

    
