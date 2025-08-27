from django.db import models
from django.contrib.auth.models import User 

class MoodEntry(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    mood_score = models.IntegerField()  
    trigger = models.CharField(max_length=255)  
    notes = models.TextField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entry for {self.user.username} on {self.created_at.strftime('%Y-%m-%d')}"
