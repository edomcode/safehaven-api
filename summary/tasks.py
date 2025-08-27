from django.db import models
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from users.models import AnonymousUser
from journal.models import JournalEntry
from mood.models import MoodEntry
from gratitude.models import GratitudeEntry
from .models import WeeklySummary

@shared_task
def generate_weekly_summaries():
    """Generates a weekly summary for all users."""
    end_date = timezone.now()
    start_date = end_date - timedelta(days=7)

    for user in AnonymousUser.objects.all():
      
        mood_entries = MoodEntry.objects.filter(user=user, created_at__range=[start_date, end_date])
        mood_average = mood_entries.aggregate(models.Avg('mood_score'))['mood_score__avg'] or 0

      
        journal_count = JournalEntry.objects.filter(user=user, created_at__range=[start_date, end_date]).count()
        gratitude_count = GratitudeEntry.objects.filter(user=user, created_at__range=[start_date, end_date]).count()

        
        WeeklySummary.objects.create(
            user=user,
            week_start=start_date.date(),
            mood_average=mood_average,
            gratitude_count=gratitude_count,
            journal_count=journal_count
        )