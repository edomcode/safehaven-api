from django.db import models
from django.contrib.auth.models import User

class WeeklySummary(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    week_start = models.DateField()

   
    mood_average = models.FloatField(null=True, blank=True)

   
    gratitude_count = models.IntegerField(default=0)

    journal_count = models.IntegerField(default=0)

    class Meta:
    
        unique_together = ('user', 'week_start')

    def __str__(self):
        return f"Summary for {self.user.username} - Week of {self.week_start}"
