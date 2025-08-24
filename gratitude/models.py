from django.db import models
from django.contrib.auth.models import User 

class GratitudeEntry(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return f"Gratitude for {self.user.username} on {self.created_at.strftime('%Y-%m-%d')}"

