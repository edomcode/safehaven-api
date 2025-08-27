from django.db import models
from django.contrib.auth.models import User

class GroundingEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type=models.CharField(max_length=100)
    impact=models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f"Entry for {self.user.username} on {self.created_at.strftime('%Y-%m-%d')}"
