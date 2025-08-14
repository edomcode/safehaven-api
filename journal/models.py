from django.db import models
from django.contrib.auth.models import User 

class JournalEntry(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

  
    content = models.TextField()

    
    emotion_tags = models.CharField(max_length=255, blank=True)

   
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entry for {self.user.username} on {self.created_at.strftime('%Y-%m-%d')}"
