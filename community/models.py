from django.db import models
from django.contrib.auth.models import User

class CommunityPost(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      
        if self.user:
            return f"Post by {self.user.username} at {self.created_at.strftime('%Y-%m-%d')}"
        return f"Anonymous post at {self.created_at.strftime('%Y-%m-%d')}"
